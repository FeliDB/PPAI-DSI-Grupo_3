package clases_entidad;

import java.util.ArrayList;
import java.util.Date;

public class CambioEstado {
    private Date fechaHoraFin;
    private Date fechaHoraInicio;
    private Estado estado;
    private Empleado empleado;
    private ArrayList<MotivoFueraServicio> motivoFueraServicios;

    public CambioEstado(Date fechaHoraFin, Date fechaHoraInicio, Estado estado, Empleado empleado, ArrayList<MotivoFueraServicio> motivoFueraServicios) {
        this.fechaHoraFin = fechaHoraFin;
        this.fechaHoraInicio = fechaHoraInicio;
        this.estado = estado;
        this.empleado = empleado;
        this.motivoFueraServicios = (motivoFueraServicios != null) ? motivoFueraServicios : new ArrayList<>();
    }
}
