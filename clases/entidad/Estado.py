class Estado:

    def __init__(self, nombre):
        self.nombre = nombre
    
    def esPendienteRevision(self):
        if self.nombre == "pendiente de revisión":
            return True