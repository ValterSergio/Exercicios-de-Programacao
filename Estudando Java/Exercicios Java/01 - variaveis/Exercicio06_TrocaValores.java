import java.util.Scanner;

public class Exercicio06_TrocaValores {

    public static void main(String[] args) {
        // Cria o Scanner para entrada do usuário
        Scanner scanner = new Scanner(System.in);

        // Solicita o primeiro número
        System.out.print("Digite o primeiro valor (A): ");
        int valorA = scanner.nextInt();

        // Solicita o segundo número
        System.out.print("Digite o segundo valor (B): ");
        int valorB = scanner.nextInt();

        // Exibe os valores antes da troca
        System.out.println("Antes da troca:");
        System.out.println("Valor A: " + valorA);
        System.out.println("Valor B: " + valorB);

        // Troca os valores usando uma variável temporária
        int temp = valorA;
        valorA = valorB;
        valorB = temp;

        // Exibe os valores depois da troca
        System.out.println("Depois da troca:");
        System.out.println("Valor A: " + valorA);
        System.out.println("Valor B: " + valorB);

        // Fecha o scanner
        scanner.close();
    }
}
