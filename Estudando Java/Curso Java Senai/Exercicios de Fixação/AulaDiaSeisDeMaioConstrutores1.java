class Construtor {
    private String nome;
    private int idade;

    public Construtor(String nome){
        this.nome = nome;
        this.idade = 18;
    }

    public void setNome(String nome){
        this.nome = nome;
    }
    public void setIdade(int idade){
        this.idade = idade;
    }

    public void exibir(){
        System.out.println("Nome: " + this.nome);
        System.out.println("Idade: " + this.idade);
    }
}

public class AulaDiaSeisDeMaioConstrutores1 {

    public static void main(String[] args) {
        Construtor p1 = new Construtor("valter");
        Construtor p2 = new Construtor("Wando");
        
        // metodos padrões
        p1.exibir();
        p2.exibir();

        // trocar metodos
        p1.setIdade(30);
        p2.setIdade(26);
        
        // Exibir metodos
        p1.exibir();
        p2.exibir();


    }
    
} 