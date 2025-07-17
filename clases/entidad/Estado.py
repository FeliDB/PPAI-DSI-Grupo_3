class Estado:

    def __init__(self, nombre, ambito):
        self.nombre = nombre
        self.ambito = ambito
    
    def esAmbitoEventoSismico(self):
        if self.ambito == "evento":
            return True

    def esBloqueadoEnRevision(self):
        if self.nombre == "bloqueado en revision":
            return True
    
    def esRechazado(self):
        if self.nombre == "rechazado":
            return True
    
    def cambiarEstadoBloqueado(self):
        self.nombre = "bloqueado en revision"
    
    def cambiarEstadoRechazado(self):
        self.nombre = "rechazado"