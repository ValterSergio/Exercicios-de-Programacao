class Pessoa{
    private String nome;
    private int idade;

    public Pessoa(String nome, int idade){
        this.nome = nome;
        this.idade = idade;
    }

    public String getNome(){
        return nome;
    }

    public int getIdade(){
        return idade;
    }

    public void setIdade(int novaIdade){
        if (novaIdade <= 0){
            System.out.println("Idade não alterada");
        } else {
            this.idade = novaIdade;
            System.out.println("Idade alterada com Sucesso");
        }
    }
}

public class exercicio_1 {
    public static void main(String[] args) {
        Pessoa p1 = new Pessoa("Diogo", 98);
        p1.setIdade(-5); // erro
        p1.setIdade((32));
        System.out.println("Nome: " + p1.getNome());
        System.out.println("Idade: " + p1.getIdade());
    
    }
}