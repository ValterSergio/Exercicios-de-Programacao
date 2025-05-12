class Animal {
    private String nome;
    private int idade;
    
    public Animal(String nome, int idade){
        this.nome = nome;
        this.idade = idade;
    }

    public String getNome(){
        return this.nome;
    }

    public void setNome(String novoNome){
        this.nome = novoNome;
    }

    public int getIdade(){
        return this.idade;
    }

    public void setIdade(int novaIdade){
        if (novaIdade > 0 && novaIdade < 100) {
            this.idade = novaIdade;
        }
    }

    public void emitirSom(){
        System.out.println("Estou fazendo um som");
    }

    public void exibirDados(){
        System.out.printf("Olá, eu sou %s, tenho %d anos. ", this.nome, this.idade);
    }
}

class Leao extends Animal{
    private String territorio;

    public Leao(String nome, int idade, String territorio){
        super(nome, idade);
        this.territorio = territorio;


    }

    public String getTerritorio(){
        return this.territorio;
    }

    public void setTerritorio(String novoTerritorio){
        this.territorio = novoTerritorio;
    }

    public void emitirSom(){ // usando polimorfismo
        System.out.println("Rugindo ( leão )");
    }

    public void exibirDados(){
        super.exibirDados();
        System.out.println("Meu territorio é " + this.territorio);
    }

}

class Papagaio extends Animal{
    private int vocabulario;

    public Papagaio(String nome, int idade, int vocabulario){
        super(nome, idade);
        this.vocabulario = vocabulario;
    }

    public int getVocabulario(){
        return this.vocabulario;
    }

    public void setVocabulario(int novoVocabulario){
        if (novoVocabulario > 0) {
            this.vocabulario = novoVocabulario;
        }
    }

    public void falar(String msg){
        System.out.println("Papagaio Falando: " + msg);
    }

    public void emitirSom(){
        System.out.println("Estou falando, sou um papagaio");
    }

    public void exibirDados(){
        super.exibirDados();

    }
}

public class AulaDiaSeteDeMaioHerancaFixacao {

    public static void main(String[] args) {
        Leao leao = new Leao("Valter", 30, "Brasileiro");
        leao.emitirSom();
        leao.exibirDados();
        System.out.println();

        Papagaio papagaio = new Papagaio("Valter", 28, 5);
        papagaio.emitirSom();
        papagaio.falar("Eu sou um Papagaio");
        papagaio.exibirDados();


    }
}