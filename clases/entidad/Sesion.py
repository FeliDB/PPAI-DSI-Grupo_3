import sys
import os

root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

if root_path not in sys.path:
    sys.path.insert(0, root_path)

from entidad.Empleado import Empleado

class Sesion:

    def __init__(self, empleado):
        self.empleado = empleado