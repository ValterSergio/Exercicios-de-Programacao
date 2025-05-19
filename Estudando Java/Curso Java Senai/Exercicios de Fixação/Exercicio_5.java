// Classe base Forma
class Forma {
    public double calcularArea() {
        return 0;
    }
}

// Classe Quadrado que herda de Forma
class Quadrado extends Forma {
    private double lado;

    public Quadrado(double lado) {
        this.lado = lado;
    }

    @Override
    public double calcularArea() {
        return lado * lado;
    }
}

// Classe Circulo que herda de Forma
class Circulo extends Forma {
    private double raio;

    public Circulo(double raio) {
        this.raio = raio;
    }

    @Override
    public double calcularArea() {
        return Math.PI * raio * raio;
    }
}

// Classe principal com o main
public class Exercicio_5 {
    public static void main(String[] args) {
        // Polimorfismo: objetos do tipo Forma
        Forma quadrado = new Quadrado(5);
        Forma circulo = new Circulo(3);

        // Exibindo áreas
        System.out.println("Área do quadrado: " + quadrado.calcularArea());
        System.out.println("Área do círculo: " + circulo.calcularArea());
    }
}
