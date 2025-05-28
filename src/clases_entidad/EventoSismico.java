package clases_entidad;

import java.util.ArrayList;
import java.util.Date;

public class EventoSismico {
    private Date fechaHoraFin;
    private Date fechaHoraOcurrencia;
    private float latitudEpicentro;
    private float latitudHipocentro;
    private float longitudEpicentro;
    private float longitudHipocentro;
    private float valorMagnitud;
    private ClasificacionSismo clasificacion;
    private MagnitudRicher magnitud;
    private OrigenDeGeneracion origenGeneracion;
    private AlcanceSismo alcanceSismo;
    private Estado estadoActual;
    private ArrayList<CambioEstado> cambioEstado;
    private SerieTemporal serieTemporal;



    public EventoSismico(Date fechaHoraFin, Date fechaHoraOcurrencia, float latitudEpicentro, float latitudHipocentro, float longitudEpicentro, float longitudHipocentro, float valorMagnitud, ClasificacionSismo clasificacion, MagnitudRicher magnitud, OrigenDeGeneracion origenGeneracion, AlcanceSismo alcanceSismo, Estado estadoActual, ArrayList<CambioEstado> cambioEstado, SerieTemporal serieTemporal) {
        this.fechaHoraFin = fechaHoraFin;
        this.fechaHoraOcurrencia = fechaHoraOcurrencia;
        this.latitudEpicentro = latitudEpicentro;
        this.latitudHipocentro = latitudHipocentro;
        this.longitudEpicentro = longitudEpicentro;
        this.longitudHipocentro = longitudHipocentro;
        this.valorMagnitud = valorMagnitud;
        this.clasificacion = clasificacion;
        this.magnitud = magnitud;
        this.origenGeneracion = origenGeneracion;
        this.alcanceSismo = alcanceSismo;
        this.estadoActual = estadoActual;
        this.cambioEstado = cambioEstado;
        this.serieTemporal = serieTemporal;
    }
}
