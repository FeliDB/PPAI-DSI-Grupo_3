package clases_entidad;

public class Empleado {
    private String apellido;
    private String mail;
    private String nombre;
    private String telefono;
    private Rol rol;

    public Empleado(String apellido, String mail, String nombre, String telefono, Rol rol) {
        this.apellido = apellido;
        this.mail = mail;
        this.nombre = nombre;
        this.telefono = telefono;
        this.rol = rol;
    }
}
