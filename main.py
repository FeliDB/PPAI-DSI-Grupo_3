# main.py
import sys
import os

# Asegurar rutas para los imports
sys.path.append("clases")
root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'clases'))
if root_path not in sys.path:
    sys.path.insert(0, root_path)

from clases.boundary.PantRegResRevManual import PantRegResRevManual
from clases.control.GestorRegResRevManual import GestorRegResRevManual
from clases.entidad.EventoSismico import EventoSismico
from clases.entidad.CambioEstado import CambioEstado
from clases.entidad.SerieTemporal import SerieTemporal
from clases.entidad.AlcanceSismo import AlcanceSismo
from clases.entidad.ClasificacionSismo import ClasificacionSismo
from clases.entidad.OrigenDeGeneracion import OrigenDeGeneracion
from clases.entidad.Estado import Estado  # NUEVO IMPORT

# Crear instancias de Estado
estados = [
    Estado("pendiente de revisión"),
    Estado("pendiente de cierre"),
    Estado("bloqueado en revisión"),
    Estado("derivado a experto"),
    Estado("confirmado"),
    Estado("rechazado")
]

# Helper para encontrar estado por nombre
def obtener_estado(nombre):
    for e in estados:
        if e.nombre == nombre:
            return e
    return None

# Crear eventos e inicializar objetos necesarios
cambio_estado_vacio = []
serie_temporal_vacia = []
alcance_dummy = AlcanceSismo("cercano", "a")
clasificacion_dummy = ClasificacionSismo(59, 62, "grave")
origen_dummy = OrigenDeGeneracion("a", "a")

evento1 = EventoSismico("2025-06-13 09:10:00", "2025-06-13 08:55:00", -31.4201, -31.4255, -64.1888, obtener_estado("pendiente de revisión"), -64.1923, 5.2, cambio_estado_vacio, serie_temporal_vacia, alcance_dummy, clasificacion_dummy, origen_dummy)
evento2 = EventoSismico("2024-11-01 16:45:00", "2024-11-01 16:30:00", -33.0345, -33.0400, -68.8458, obtener_estado("confirmado"), -68.8501, 4.7, cambio_estado_vacio, serie_temporal_vacia, alcance_dummy, clasificacion_dummy, origen_dummy)
evento3 = EventoSismico("2023-03-22 04:05:00", "2023-03-22 03:50:00", -27.4741, -27.4700, -66.8852, obtener_estado("rechazado"), -66.8800, 6.1, cambio_estado_vacio, serie_temporal_vacia, alcance_dummy, clasificacion_dummy, origen_dummy)
evento4 = EventoSismico("2022-08-10 22:40:00", "2022-08-10 22:30:00", -24.7812, -24.7800, -65.4090, obtener_estado("derivado a experto"), -65.4100, 3.8, cambio_estado_vacio, serie_temporal_vacia, alcance_dummy, clasificacion_dummy, origen_dummy)

# Crear el gestor y pasarle los estados
gestor = GestorRegResRevManual()
gestor.cargarEventos([evento1, evento2, evento3, evento4])
gestor.setEstados(estados)  # NUEVO

# Crear e iniciar la pantalla
pantalla = PantRegResRevManual(gestor)
pantalla.habilitarVentana()
