class Veiculo {
    private String modelo;
    private int ano;

    public Veiculo(String modelo, int ano){
        this.modelo = modelo;
        this.ano = ano;
    }

    public String getModelo() {
        return modelo;
    }

    public void setModelo(String modelo) {
        this.modelo = modelo;
    }

    public int getAno() {
        return ano;
    }

    public void setAno(int ano) {
        this.ano = ano;
    }

    public void exibirDados(){
        System.out.print("\nVeiculo: " + this.modelo + " Ano: " + this.ano);
    }

    public void ligar() {
        System.out.println(this.getClass().getName() + " Ligando...");
    }
}

class Carro extends Veiculo {
    private int numeroDePortas;

    public Carro(String modelo, int ano, int numeroDePortas){
        super(modelo, ano);
        this.numeroDePortas = numeroDePortas;
    }

    public int getNumeroDePortas() {
        return numeroDePortas;
    }

    public void setNumeroDePortas(int numeroDePortas) {
        this.numeroDePortas = numeroDePortas;
    }

    public void tocarSom(){
        System.out.println("\n---> Tocando musica");
        System.out.println("é som de preto de Favelado ");
        System.out.println("Mas quando toca ninguém fica parado");
        System.out.println("....\n");
    }

    @Override
    public void ligar() {
        super.ligar();
    }

    @Override
    public void exibirDados() {
        super.exibirDados();
        System.out.print(" Numero de Portas: " + this.numeroDePortas + "\n");
    }
}

class Moto extends Veiculo {
    private boolean capacetePresente;

    public Moto(String modelo, int ano, boolean capacetePresente){
        super(modelo, ano);
        this.capacetePresente = capacetePresente;
    }

    public boolean isCapacetePresente() {
        return capacetePresente;
    }

    public void setCapacetePresente(boolean capacetePresente) {
        this.capacetePresente = capacetePresente;
    }

    @Override
    public void ligar() {
        super.ligar();
    }

    public void empinar(){
        System.out.println("Estou empinando !");
    }

    @Override
    public void exibirDados() {
        super.exibirDados();
        System.out.println(" Capacete: " + this.capacetePresente);
    }
}

class Caminhao extends Veiculo {
    private double capacidadeCarga;

    public Caminhao(String modelo, int ano, double capacidadeCarga){
        super(modelo, ano);
        this.capacidadeCarga = capacidadeCarga;
    }

    public double getCapacidadeCarga() {
        return capacidadeCarga;
    }

    public void setCapacidadeCarga(double capacidadeCarga) {
        this.capacidadeCarga = capacidadeCarga;
    }

    public void carregarCarga(double carga){
        this.capacidadeCarga -= carga;
    }
}

class Oficina {
    private Veiculo[] veiculosVetor;

    public Oficina(int limite){
        this.veiculosVetor = new Veiculo[limite];
    }

    public void adicionarVeiculo(Veiculo veiculo){
        boolean adicionado = false;
        int posicao = 0;

        for (int i = 0; i < veiculosVetor.length; i++) {
            if (veiculosVetor[i] == null){
                veiculosVetor[i] = veiculo;
                adicionado = true;
                posicao = i;
                break;
            }
        }

        if (adicionado && posicao != -1) {
            System.out.println("Posição do " + veiculo.getModelo() + ": " + posicao);
        } else {
            System.out.println("Falta espaço de armazenamento");
        }
    }

    public void revisarVeiculo(){
        for (Veiculo veiculo : veiculosVetor) {
            if (veiculo != null){
                veiculo.ligar();
                veiculo.exibirDados();
            }
        }
    }
}

public class AulaDiaDozeMaioTranslog {
    public static void main(String[] args) {
        System.out.println("\n---- carro ");
        Carro carro = new Carro("Chevrolet Voyage", 1999, 4);
        carro.ligar();
        carro.tocarSom();
        
        System.out.println("\n---- Moto ");
        Moto moto = new Moto("Honda Cg 125", 2002, true);
        moto.ligar();
        moto.empinar();
        
        System.out.println("\n---- Caminhão ");
        Caminhao caminhao = new Caminhao("Scania", 2025, 10);
        caminhao.ligar();
        caminhao.carregarCarga(250);
        
        System.out.println("\n---- Oficina ");
        Oficina oficina = new Oficina(10);
        oficina.adicionarVeiculo(carro);
        oficina.adicionarVeiculo(moto);
        oficina.adicionarVeiculo(caminhao);

        System.out.println("\n--- Revisão ");
        oficina.revisarVeiculo();
    }
}
