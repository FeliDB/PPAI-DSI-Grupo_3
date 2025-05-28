package clases_entidad;

import java.util.ArrayList;
import java.util.Date;

public class MuestraSismica {
    private Date fechaHoraMuestra;
    private ArrayList<DetalleMuestraSismica> detalleMuestraSismicas;

    public MuestraSismica(Date fechaHoraMuestra, ArrayList<DetalleMuestraSismica> detalleMuestraSismicas) {
        this.fechaHoraMuestra = fechaHoraMuestra;
        this.detalleMuestraSismicas = detalleMuestraSismicas;
    }
}
