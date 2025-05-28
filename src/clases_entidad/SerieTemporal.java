package clases_entidad;

import java.util.ArrayList;
import java.util.Date;

public class SerieTemporal {
    private String condicionAlarma;
    private Date fechaHoraInicioRegistroMuestras;
    private Date fechaHoraInicioRegistro;
    private float frecuenciaMuestreo;
    private ArrayList<MuestraSismica> muestraSismica;

    public SerieTemporal(String condicionAlarma, Date fechaHoraInicioRegistroMuestras, Date fechaHoraInicioRegistro, float frecuenciaMuestreo, ArrayList<MuestraSismica> muestraSismica) {
        this.condicionAlarma = condicionAlarma;
        this.fechaHoraInicioRegistroMuestras = fechaHoraInicioRegistroMuestras;
        this.fechaHoraInicioRegistro = fechaHoraInicioRegistro;
        this.frecuenciaMuestreo = frecuenciaMuestreo;
        this.muestraSismica = muestraSismica;
    }
}
