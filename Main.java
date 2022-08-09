public class Main {

    public static void main(String[] args){

        Cliente cliente1 = new Cliente(25, "Juan", "3624041289", 5233);
        Trabajador trabajador1 = new Trabajador(35, "Jose", "3644569823", 85000);

        System.out.println("--------------------------\n");
        System.out.print("Nombre: "+cliente1.getNombre()+"\n"+"Edad: "+cliente1.getEdad()+"\n"+"Telefono: "+cliente1.getTelefono()+"\n"+"Credito: "+cliente1.getCredito()+"\n");
        System.out.println("--------------------------\n");
        System.out.print("Nombre: "+trabajador1.getNombre()+"\n"+"Edad: "+trabajador1.getEdad()+"\n"+"Telefono: "+trabajador1.getTelefono()+"\n"+"Salario: "+trabajador1.getSalario()+"\n");

    }
    
}
