# main.py
import sys
import os
from datetime import datetime

from clases.boundary import PantRegResRevManual

from datetime import datetime

from clases.boundary.PantRegResRevManual import PantRegResRevManual


# Crear e iniciar la pantalla
pantalla = PantRegResRevManual()
pantalla.habilitarVentana()
print("Ruta añadida a sys.path:", os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))