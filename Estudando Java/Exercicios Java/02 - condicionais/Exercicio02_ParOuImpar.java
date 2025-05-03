import java.util.Scanner;

public class Exercicio02_ParOuImpar {

    public static void main(String[] args) {
        // Cria o Scanner para entrada do usuário
        Scanner scanner = new Scanner(System.in);

        // Solicita um número inteiro
        System.out.print("Digite um número inteiro: ");
        int numero = scanner.nextInt();

        // Verifica se o número é par ou ímpar
        if (numero % 2 == 0) {
            System.out.println("O número " + numero + " é PAR.");
        } else {
            System.out.println("O número " + numero + " é ÍMPAR.");
        }

        // Fecha o scanner
        scanner.close();
    }
}
