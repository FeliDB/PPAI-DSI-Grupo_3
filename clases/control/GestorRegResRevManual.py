from datetime import datetime
from instancias import eventosSismicos
from instancias import Sesion

class GestorRegResRevManual:
    def __init__(self):
        pass

    def buscarEventoSismicoAD(self):
        eventos_pendientes = []
        for evento in eventosSismicos:
            if evento.estado.esPendienteRevision():
                eventos_pendientes.append(evento)
        print(eventos_pendientes)
        return eventos_pendientes

    def getDatosPrincipales(self):
        eventostmp = self.buscarEventoSismicoAD()
        return [evento.getDatosPrincipales() for evento in eventostmp]
    
    def bloquearEventoSismicoYRevisar(self, evento):
        for cambio in evento.cambioEstado:
            if evento.estado.nombre == cambio.estado.nombre:
                evento.actualizarEstado(datetime.now(), datetime.now(), evento, "bloqueado en revisión", Sesion[0])
                break

    
    def buscarDatosSismicos(self, evento):
            if evento is None:
                print("[ERROR] Evento es None.")
                return []
            return evento.getDatosSismicos()
    
    def actualizarCambioEstado(self, evento, accion):
        evento.actualizarEstado(datetime.now(), datetime.now(), evento, accion, Sesion[0])
        print(evento.cambioEstado[-1])