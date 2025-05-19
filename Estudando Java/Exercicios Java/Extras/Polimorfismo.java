// Classe Pai
class Pai {
    public void a() {
        System.out.println("Chamar método pai - a()");
    }

    public void b() {
        System.out.println("Chamar método pai - b()");
    }
}

// Classe Filho que herda de Pai
class Filho extends Pai {
    @Override
    public void b() {
        System.out.println("Chamar método filho - b()");
    }

    public void c() {
        System.out.println("Chamar método filho - c()");
    }
}

// Classe principal com o método main
public class Principal {
    public static void main(String[] args) {
        Pai obj = new Filho();

        obj.a(); // Chama a() da classe Pai
        obj.b(); // Chama b() da classe Filho (polimorfismo dinâmico)
        
        // obj.c(); // ERRO! Método c() não está definido na classe Pai
        // Para chamar c(), seria necessário fazer cast: ((Filho) obj).c();
    }
}
