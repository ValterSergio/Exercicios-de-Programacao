public class Exercicio_9 {

    // Classe Cubo
    static class Cubo {
        private double aresta;

        public Cubo(double aresta) {
            this.aresta = aresta;
        }

        public double calcularVolume() {
            return Math.pow(aresta, 3);
        }

        public double calcularAreaSuperficial() {
            return 6 * Math.pow(aresta, 2);
        }
    }

    // Classe Esfera
    static class Esfera {
        private double raio;

        public Esfera(double raio) {
            this.raio = raio;
        }

        public double calcularVolume() {
            return (4.0 / 3.0) * Math.PI * Math.pow(raio, 3);
        }

        public double calcularAreaSuperficial() {
            return 4 * Math.PI * Math.pow(raio, 2);
        }
    }

    // Método main
    public static void main(String[] args) {
        // Criando instâncias
        Cubo cubo = new Cubo(3);       // Aresta = 3
        Esfera esfera = new Esfera(2); // Raio = 2

        // Resultados do cubo
        System.out.println("CUBO");
        System.out.println("Volume: " + cubo.calcularVolume());
        System.out.println("Área superficial: " + cubo.calcularAreaSuperficial());

        // Resultados da esfera
        System.out.println("\nESFERA");
        System.out.println("Volume: " + esfera.calcularVolume());
        System.out.println("Área superficial: " + esfera.calcularAreaSuperficial());
    }
}
