from Estado import Estado
from CambioEstado import CambioEstado
from SerieTemporal import SerieTemporal
from AlcanceSismo import AlcanceSismo
from ClasificacionSismo import ClasificacionSismo
from OrigenDeGeneracion import OrigenDeGeneracion


class EventoSismico:
    def __init__(self, fechaHoraFin, fechaHoraOcurrencia, latitudEpicentro, latitudHipocentro, longitudEpicentro, longitudHipocentro, valorMagnitud):
        self.fechaHoraFin = fechaHoraFin
        self.fechaHoraOcurrencia = fechaHoraOcurrencia
        self.latitudEpicentro = latitudEpicentro
        self.latitudHipocentro = latitudHipocentro
        self.longitudEpicentro = longitudEpicentro
        self.longitudHipocentro = longitudHipocentro
        self.valorMagnitud = valorMagnitud