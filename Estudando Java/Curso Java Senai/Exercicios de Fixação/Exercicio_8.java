public class Exercicio_8 {

    // Classe Calculadora com métodos estáticos
    static class Calculadora {
        // Construtor privado para impedir instância
        private Calculadora() {}

        // Soma
        public static double somar(double a, double b) {
            return a + b;
        }

        // Subtração
        public static double subtrair(double a, double b) {
            return a - b;
        }

        // Multiplicação
        public static double multiplicar(double a, double b) {
            return a * b;
        }

        // Divisão com tratamento de erro
        public static double dividir(double a, double b) {
            if (b == 0) {
                throw new IllegalArgumentException("Divisão por zero não é permitida.");
            }
            return a / b;
        }
    }

    // Método main para demonstrar operações
    public static void main(String[] args) {
        // Operações
        double resultadoSoma = Calculadora.somar(10, 5);
        double resultadoDivisao = 0;

        try {
            resultadoDivisao = Calculadora.dividir(20, 4);
        } catch (IllegalArgumentException e) {
            System.out.println("Erro: " + e.getMessage());
        }

        // Exibindo resultados
        System.out.println("Resultado da soma: " + resultadoSoma);
        System.out.println("Resultado da divisão: " + resultadoDivisao);
    }
}
