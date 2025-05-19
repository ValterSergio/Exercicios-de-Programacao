class Animal {
    private String nome;
    private String raca;
    private int idade;

    public Animal(String nome, String raca, int idade){
        this.nome = nome;
        this.raca = raca;
        this.idade = idade;
    }

    public void emitirSom(){
        System.out.println("Emitindo Som");
    }
}

class Cachorro extends Animal {
    public Cachorro(String nome, String raca, int idade){
        super(nome, raca, idade);
    }

    public void emitirSom(){
        System.out.println("AU AU");
    }
}

class Gato extends Animal {
    public Gato(String nome, String raca, int idade){
        super(nome, raca, idade);
    }

    public void emitirSom(){
        System.out.println("MIAU MIAU");
    }
}

public class exercicio_3 {
    public static void main(String[] args) {
        String nome = "cao";
        String raca = "animal";
        int idade = 3;
        Animal animal = new Animal(nome, raca, idade);
        Animal cao = new Cachorro(nome, raca, idade);
        Animal gato = new Gato(nome, raca, idade);

        Animal animais[] = new Animal[3];
        animais[0] = animal;
        animais[1] = cao;
        animais[2] = gato;

        for (int i = 0; i < animais.length; i++) {
            animais[i].emitirSom();
        }
    }
}
