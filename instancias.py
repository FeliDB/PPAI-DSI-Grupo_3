from clases.entidad.EventoSismico import EventoSismico
from clases.entidad.CambioEstado import CambioEstado
from clases.entidad.SerieTemporal import SerieTemporal
from clases.entidad.MuestraSismica import MuestraSismica
from clases.entidad.DetalleMuestraSismica import DetalleMuestraSismica
from clases.entidad.AlcanceSismo import AlcanceSismo
from clases.entidad.ClasificacionSismo import ClasificacionSismo
from clases.entidad.OrigenDeGeneracion import OrigenDeGeneracion
from clases.entidad.Estado import Estado
from clases.entidad.Usuario import Usuario
from clases.entidad.Sesion import Sesion

from datetime import datetime, timedelta

# Crear instancias de Estado
estados = [
    Estado("pendiente de revisión", "evento"),
    Estado("pendiente de cierre", "evento"),
    Estado("bloqueado en revisión", "evento"),
    Estado("derivado a experto", "evento"),
    Estado("confirmado", "evento"),
    Estado("rechazado", "evento")
]

# Usuarios / empleados que cambian estados
Usuarios = [Usuario("usuario123", "12345"), Usuario("usuario246", "24680")]
Empleados = [Usuarios[0], Usuarios[1]]
SesionActual = [Usuarios[0]]

# Crear instancias de DetalleMuestraSismica
detalle1 = DetalleMuestraSismica(valor=0.12)
detalle2 = DetalleMuestraSismica(valor=0.34)
detalle3 = DetalleMuestraSismica(valor=0.56)
detalle4 = DetalleMuestraSismica(valor=0.78)

# Crear instancias de MuestraSismica
muestra1 = MuestraSismica(detalle1)
muestra2 = MuestraSismica(detalle2)
muestra3 = MuestraSismica(detalle3)
muestra4 = MuestraSismica(detalle4)

# Asociar muestras a cada SerieTemporal
muestrasSerie1 = [muestra1, muestra2]
muestrasSerie2 = [muestra2, muestra3]
muestrasSerie3 = [muestra3, muestra4]
muestrasSerie4 = [muestra1, muestra4]

# Crear instancias de SerieTemporal para cada evento
serie1 = SerieTemporal(
    condicionAlarma="Alarma baja",
    fechaHoraRegistroMuestras=datetime.now() - timedelta(minutes=15),
    fechaHoraRegistro=datetime.now(),
    frecuenciaMuestreo=100,
    muestraSismica=muestrasSerie1
)
serie2 = SerieTemporal(
    condicionAlarma="Alarma media",
    fechaHoraRegistroMuestras=datetime.now() - timedelta(minutes=30),
    fechaHoraRegistro=datetime.now(),
    frecuenciaMuestreo=200,
    muestraSismica=muestrasSerie2
)
serie3 = SerieTemporal(
    condicionAlarma="Alarma alta",
    fechaHoraRegistroMuestras=datetime.now() - timedelta(minutes=45),
    fechaHoraRegistro=datetime.now(),
    frecuenciaMuestreo=150,
    muestraSismica=muestrasSerie3
)
serie4 = SerieTemporal(
    condicionAlarma="Alarma crítica",
    fechaHoraRegistroMuestras=datetime.now() - timedelta(minutes=60),
    fechaHoraRegistro=datetime.now(),
    frecuenciaMuestreo=300,
    muestraSismica=muestrasSerie4
)

# Crear instancias de EventoSismico con cambios de estado y series temporales
eventosSismicos = [
    EventoSismico(
        fechaHoraFin=datetime.now() + timedelta(hours=1),
        fechaHoraOcurrencia=datetime.now(),
        latitudEpicentro=-34.60,
        latitudHipocentro=-34.61,
        longitudEpicentro=-58.38,
        estado=estados[0],
        longitudHipocentro=-58.39,
        valorMagnitud=4.5,
        cambioEstado=[
            CambioEstado(
                fechaHoraFin=datetime.now(),
                fechaHoraInicio=datetime.now() - timedelta(hours=1),
                estado=estados[5],
                usuario=Usuarios[0]
            ),
            CambioEstado(
                fechaHoraFin=datetime.now() + timedelta(minutes=30),
                fechaHoraInicio=datetime.now(),
                estado=estados[0],
                usuario=Usuarios[1]
            )
        ],
        serieTemporal=[serie1],
        alcanceSismo=AlcanceSismo("Alcance local", "Local"),
        clasificacionSismo=ClasificacionSismo(0, 70, "Superficial"),
        origenGeneracion=OrigenDeGeneracion("Origen tectónico", "Tectónico")
    ),
    EventoSismico(
        fechaHoraFin=datetime.now() + timedelta(hours=2),
        fechaHoraOcurrencia=datetime.now(),
        latitudEpicentro=-33.00,
        latitudHipocentro=-33.01,
        longitudEpicentro=-56.15,
        estado=estados[1],
        longitudHipocentro=-56.16,
        valorMagnitud=5.2,
        cambioEstado=[
            CambioEstado(
                fechaHoraFin=datetime(2025, 6, 16, 14, 30, 0),
                fechaHoraInicio=datetime(2025, 6, 16, 13, 30, 0),
                estado=estados[2],
                usuario=Usuarios[0]
            ),
            CambioEstado(
                fechaHoraFin=datetime.now(),
                fechaHoraInicio=datetime(2025, 6, 16, 14, 30, 0),
                estado=estados[1],
                usuario=Usuarios[1]
            )
        ],
        serieTemporal=[serie2],
        alcanceSismo=AlcanceSismo("Alcance regional", "Regional"),
        clasificacionSismo=ClasificacionSismo(70, 300, "Intermedio"),
        origenGeneracion=OrigenDeGeneracion("Origen volcánico", "Volcánico")
    ),
    EventoSismico(
        fechaHoraFin=datetime.now() + timedelta(hours=3),
        fechaHoraOcurrencia=datetime.now(),
        latitudEpicentro=-31.40,
        latitudHipocentro=-31.42,
        longitudEpicentro=-64.18,
        estado=estados[2],
        longitudHipocentro=-64.20,
        valorMagnitud=3.8,
        cambioEstado=[
            CambioEstado(
                fechaHoraFin=datetime.now() - timedelta(minutes=20),
                fechaHoraInicio=datetime.now() - timedelta(hours=2),
                estado=estados[0],
                usuario=Usuarios[1]
            ),
            CambioEstado(
                fechaHoraFin=datetime.now(),
                fechaHoraInicio=datetime.now() - timedelta(minutes=20),
                estado=estados[2],
                usuario=Usuarios[0]
            )
        ],
        serieTemporal=[serie3],
        alcanceSismo=AlcanceSismo("Alcance local", "Local"),
        clasificacionSismo=ClasificacionSismo(0, 70, "Superficial"),
        origenGeneracion=OrigenDeGeneracion("Origen artificial", "Artificial")
    ),
    EventoSismico(
        fechaHoraFin=datetime.now() + timedelta(hours=4),
        fechaHoraOcurrencia=datetime.now(),
        latitudEpicentro=-35.00,
        latitudHipocentro=-35.01,
        longitudEpicentro=-62.00,
        estado=estados[3],
        longitudHipocentro=-62.02,
        valorMagnitud=6.1,
        cambioEstado=[
            CambioEstado(
                fechaHoraFin=datetime.now() - timedelta(hours=1),
                fechaHoraInicio=datetime.now() - timedelta(hours=3),
                estado=estados[1],
                usuario=Usuarios[0]
            ),
            CambioEstado(
                fechaHoraFin=datetime.now(),
                fechaHoraInicio=datetime.now() - timedelta(hours=1),
                estado=estados[3],
                usuario=Usuarios[1]
            )
        ],
        serieTemporal=[serie4],
        alcanceSismo=AlcanceSismo("Alcance regional", "Regional"),
        clasificacionSismo=ClasificacionSismo(70, 300, "Intermedio"),
        origenGeneracion=OrigenDeGeneracion("Origen tectónico", "Tectónico")
    ),
    EventoSismico(
        fechaHoraFin=datetime.now() + timedelta(hours=4),
        fechaHoraOcurrencia=datetime.now(),
        latitudEpicentro=-31.00,
        latitudHipocentro=-61.01,
        longitudEpicentro=-31.00,
        estado=estados[0],
        longitudHipocentro=-531.3,
        valorMagnitud=3,
        cambioEstado=[
            CambioEstado(
                fechaHoraFin=datetime.now() - timedelta(hours=1),
                fechaHoraInicio=datetime.now() - timedelta(hours=3),
                estado=estados[0],
                usuario=Usuarios[1]
            ),
            CambioEstado(
                fechaHoraFin=datetime.now(),
                fechaHoraInicio=datetime.now() - timedelta(hours=1),
                estado=estados[3],
                usuario=Usuarios[1]
            )
        ],
        serieTemporal=[serie3],
        alcanceSismo=AlcanceSismo("Alcance regional", "Regional"),
        clasificacionSismo=ClasificacionSismo(70, 300, "Intermedio"),
        origenGeneracion=OrigenDeGeneracion("Origen tectónico", "Tectónico")
    )
]