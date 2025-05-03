import java.util.Scanner;

public class Exercicio05_Fatorial {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Solicita o número para calcular o fatorial
        System.out.print("Digite um número inteiro positivo: ");
        int numero = scanner.nextInt();

        long fatorial = 1;

        // Cálculo do fatorial com for decrescente
        for (int i = numero; i >= 1; i--) {
            fatorial *= i;
        }

        // Exibe o resultado
        System.out.println("O fatorial de " + numero + " é: " + fatorial);

        scanner.close();
    }
}
