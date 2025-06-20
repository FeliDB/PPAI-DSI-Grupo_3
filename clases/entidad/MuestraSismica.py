import sys
import os

root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

if root_path not in sys.path:
    sys.path.insert(0, root_path)

from entidad.DetalleMuestraSismica import DetalleMuestraSismica

class MuestraSismica:

    def __init__(self, detalleMuestraSismica):
        self.detalleMuestraSismica = detalleMuestraSismica

    def __str__(self):
        return f"Tiempo: {self.tiempo}, Amplitud: {self.amplitud}, Frecuencia: {self.frecuencia}"