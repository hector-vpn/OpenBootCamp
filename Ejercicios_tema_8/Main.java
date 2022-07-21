package Ejercicios_tema_8;
public class Main{
    public static void main(String[] args) {

        Persona persona1 = new Persona();

        persona1.setEdad(23);
        persona1.setNombre("Juan");
        persona1.setTelefono(158539);

        System.out.println(persona1.getNombre()+"\n"+persona1.getEdad()+"\n"+persona1.getTelefono());

        
    }
}

class Persona{

    private int edad;
    private String nombre;
    private int telefono;

    public void setEdad(int edad){
        this.edad = edad;
    }

    public int getEdad(){
        return edad;
    }

    public void setNombre(String nombre){
        this.nombre = nombre;
    }

    public String getNombre(){
        return nombre;
    }

    public void setTelefono(int telefono){
        this.telefono = telefono;
    }

    public int getTelefono(){
        return telefono;
    }
}