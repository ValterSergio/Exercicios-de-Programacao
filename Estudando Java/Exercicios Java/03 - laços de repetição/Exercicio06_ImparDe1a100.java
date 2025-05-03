public class Exercicio06_ImparDe1a100 {

    public static void main(String[] args) {

        System.out.println("Números ímpares de 1 a 100:");

        // Loop de 1 a 100
        for (int i = 1; i <= 100; i++) {
            // Se o número for ímpar (resto da divisão por 2 é diferente de 0)
            if (i % 2 != 0) {
                System.out.print(i + " ");
            }
        }

        System.out.println(); // Quebra de linha no final
    }
}
