import java.util.Scanner;

public class Exercicio02_SomaDoisNumeros {

    public static void main(String[] args) {
        // Cria o Scanner para ler dados do teclado
        Scanner scanner = new Scanner(System.in);

        // Solicita o primeiro número
        System.out.print("Digite o primeiro número inteiro: ");
        int numero1 = scanner.nextInt();

        // Solicita o segundo número
        System.out.print("Digite o segundo número inteiro: ");
        int numero2 = scanner.nextInt();

        // Calcula a soma dos dois números
        int soma = numero1 + numero2;

        // Exibe o resultado da soma
        System.out.println("A soma de " + numero1 + " + " + numero2 + " é: " + soma);

        // Fecha o Scanner
        scanner.close();
    }
}
