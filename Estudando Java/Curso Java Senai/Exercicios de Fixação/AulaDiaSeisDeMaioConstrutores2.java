class Construtor {
    private String nome;
    private int idade;

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

public class AulaDiaSeisDeMaioConstrutores2 {

    public static void main(String[] args) {
        Construtor p1 = new Construtor();

        p1.setIdade(31);
        p1.setNome("valter");
        p1.exibir();
    
        Construtor p2 = new Construtor();

        // p2.setIdade(25);
        p2.setNome("Jorge Salve");
        p2.exibir();
    
    }
    
}