from clases.entidad.CambioEstado import CambioEstado


class EventoSismico:
    def __init__(
        self,
        fechaHoraFin,
        fechaHoraOcurrencia,
        latitudEpicentro,
        latitudHipocentro,
        longitudEpicentro,
        estado,
        longitudHipocentro,
        valorMagnitud,
        cambioEstado,              # Lista de CambioEstado
        serieTemporal,             # Lista de SerieTemporal
        alcanceSismo,              # Instancia de AlcanceSismo
        clasificacionSismo,        # Instancia de ClasificacionSismo
        origenGeneracion           # Instancia de OrigenDeGeneracion
    ):
        self.fechaHoraFin = fechaHoraFin
        self.estado = estado
        self.fechaHoraOcurrencia = fechaHoraOcurrencia
        self.latitudEpicentro = latitudEpicentro
        self.latitudHipocentro = latitudHipocentro
        self.longitudEpicentro = longitudEpicentro
        self.longitudHipocentro = longitudHipocentro
        self.valorMagnitud = valorMagnitud
        self.cambioEstado = cambioEstado or []
        self.serieTemporal = serieTemporal or []
        self.alcanceSismo = alcanceSismo
        self.clasificacionSismo = clasificacionSismo
        self.origenGeneracion = origenGeneracion

    def getDatosPrincipales(self):
        return {
            "fechaHoraFin": self.fechaHoraFin,
            "fechaHoraOcurrencia": self.fechaHoraOcurrencia,
            "latitudEpicentro": self.latitudEpicentro,
            "latitudHipocentro": self.latitudHipocentro,
            "longitudEpicentro": self.longitudEpicentro,
            "longitudHipocentro": self.longitudHipocentro,
            "valorMagnitud": self.valorMagnitud,
            "estado": str(self.estado),  # Requiere que Estado tenga un __str__ representativo
            "alcanceSismo": str(self.alcanceSismo),
            "clasificacionSismo": str(self.clasificacionSismo),
            "origenGeneracion": str(self.origenGeneracion),
            "cambioEstado": [str(c) for c in self.cambioEstado],
            "serieTemporal": [str(s) for s in self.serieTemporal]
        }


    def actualizarEstado(self, fechaHoraInicio, fechaHoraFin, evento, estado, empleado):
        evento.cambioEstado.append(CambioEstado(fechaHoraInicio, fechaHoraFin, estado, evento.cambioEstado[-1].empleado))
        print(evento.cambioEstado[-1])

    
    def getDatosSismicos(self):
        print(f"[DEBUG] Series en evento: {len(self.serieTemporal)}")
        return [serie.getMuestras() for serie in self.serieTemporal]