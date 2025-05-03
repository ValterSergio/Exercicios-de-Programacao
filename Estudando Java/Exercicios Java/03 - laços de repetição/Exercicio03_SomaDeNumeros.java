import java.util.Scanner;

public class Exercicio03_SomaDeNumeros {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Solicita até qual número somar
        System.out.print("Digite um número positivo: ");
        int numeroFinal = scanner.nextInt();

        int soma = 0; // Acumulador

        // Soma de 1 até o número informado
        for (int i = 1; i <= numeroFinal; i++) {
            soma += i;
        }

        // Exibe o resultado da soma
        System.out.println("A soma de 1 até " + numeroFinal + " é: " + soma);

        scanner.close();
    }
}
