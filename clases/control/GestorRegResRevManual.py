from datetime import datetime
from instancias import eventosSismicos
from instancias import SesionActual
from instancias import estados
from entidad.EventoSismico import EventoSismico

class GestorRegResRevManual:
    def __init__(self):
        self.estado = None
        self.eventos = []
        self.usuarioLogueado = None

    def setEstado(self, estado):
        self.estado = estado
    
    def setUsuarioLogueado(self, usuarioLogueado):
        self.usuarioLogueado = usuarioLogueado




    def buscarEventoSismicoAD(self):
        for estadoPR in estados:
            if estadoPR.nombre == "pendiente de revisión":
                self.estado = estadoPR.nombre
                print(self.estado)
                break
        
        for eventosPR in eventosSismicos:
            if eventosPR.estado.nombre == self.estado:
                self.eventos.append(eventosPR)
        
        return self.eventos
    

    def buscarEstadoBloqueado(self):
        for estadoBR in estados:
            if estadoBR.esAmbitoEventoSismico():
                if estadoBR.esBloqueadoEnRevision():
                    return estadoBR.nombre
    
    def buscarEstadoRechazado(self):
        for estadoBR in estados:
            if estadoBR.esAmbitoEventoSismico():
                if estadoBR.esRechazado():
                    return estadoBR.nombre
    
    def tomarFechaHoraActual(self):
        fecha_hora_actual = datetime.now()
        return fecha_hora_actual
    
    def buscarUsuarioLogueado(self):
        self.setUsuarioLogueado(SesionActual.getUsuarioLogueado())
        print(self.setUsuarioLogueado(SesionActual.getUsuarioLogueado()))


    def bloquearEventoSismico(self, evento):
        evento.bloquearEventoSismico(self.estado, self.usuarioLogueado)
        
    def getDatosPrincipales(self):
        eventostmp = self.buscarEventoSismicoAD()
        return [evento.getDatosPrincipales() for evento in eventostmp]

    def buscarDatosSismicos(self, evento):
        if evento is None:
            print("[ERROR] Evento es None.")
            return []
        return evento.getDatosSismicos()


    def rechazarEventoSismico(self, evento):
        estadoRechazado = self.buscarEstadoRechazado()
        evento.rechazarEventoSismico(estadoRechazado, self.usuarioLogueado)
