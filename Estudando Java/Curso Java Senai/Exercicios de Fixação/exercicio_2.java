class Veiculo {
    private String marca;
    private String modelo;

    public Veiculo (String marca, String modelo){
        this.marca = marca;
        this.modelo = modelo;
    }

    public String getMarca(){
        return marca;
    }

    public String getModelo(){
        return modelo;
    }

    public String mostrarDetalhes(){
        return "\nMarca: " + getMarca() + " \nModelo: " + getModelo();
    }
}

class Carro extends Veiculo {
    private int numPortas;

    public Carro(String marca, String modelo, int numPortas){
        super(marca, modelo);
        this.numPortas = numPortas;
    }

    public int getPorta(){
        return numPortas;
    }
    public String mostrarDetalhes(){
        return super.mostrarDetalhes() + " \nPortas: " + getPorta();
    }

}


public class exercicio_2 {
    public static void main(String[] args) {
        String marca = "VolksWagen";
        String modelo = "gol";
        int numPortas = 2;
        Veiculo carro = new Carro(marca, modelo, numPortas);
        String saida = carro.mostrarDetalhes();
        System.out.println(saida);
    }   
}
