class SerieTemporal:
    def __init__(self, condicionAlarma, fechaHoraRegistroMuestras, fechaHoraRegistro, frecuenciaMuestreo, muestraSismica):
        self.condicionAlarma = condicionAlarma
        self.fechaHoraRegistroMuestras = fechaHoraRegistroMuestras
        self.fechaHoraRegistro = fechaHoraRegistro
        self.frecuenciaMuestreo = frecuenciaMuestreo
        self.muestraSismica = muestraSismica

    def getMuestras(self):
        print(f"[DEBUG] Muestras obtenidas: {self.muestraSismica}")
        return self.muestraSismica