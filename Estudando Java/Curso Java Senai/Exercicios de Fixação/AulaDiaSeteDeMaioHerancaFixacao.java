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

    public Leao()
}

public class AulaDiaSeteDeMaioHerancaFixacao {

    public static void main(String[] args) {
        
    }
}