import sys
import os

root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

if root_path not in sys.path:
    sys.path.insert(0, root_path)

from entidad.Estado import Estado
from entidad.Empleado import Empleado

class CambioEstado:
    def __init__(self, fechaHoraInicio, fechaHoraFin, estado, empleado):
        self.fechaHoraInicio = fechaHoraInicio
        self.fechaHoraFin = fechaHoraFin
        self.estado = estado
        self.empleado = empleado
