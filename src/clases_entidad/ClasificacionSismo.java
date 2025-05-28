package clases_entidad;

public class ClasificacionSismo {
    private float kmProfundidadHasta;
    private float kmProfundidadDesde;
    private String nombre;

    public ClasificacionSismo(float kmProfundidadHasta, float kmProfundidadDesde, String nombre) {
        this.kmProfundidadHasta = kmProfundidadHasta;
        this.kmProfundidadDesde = kmProfundidadDesde;
        this.nombre = nombre;
    }
}
