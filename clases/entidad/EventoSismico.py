import sys
import os

root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

if root_path not in sys.path:
    sys.path.insert(0, root_path)

from entidad.Estado import Estado
from entidad.CambioEstado import CambioEstado
from entidad.SerieTemporal import SerieTemporal
from entidad.AlcanceSismo import AlcanceSismo
from entidad.ClasificacionSismo import ClasificacionSismo
from entidad.OrigenDeGeneracion import OrigenDeGeneracion


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
