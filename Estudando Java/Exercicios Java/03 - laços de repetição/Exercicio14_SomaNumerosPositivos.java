import java.util.Scanner;

public class Exercicio14_SomaNumerosPositivos {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int soma = 0;

        System.out.println("Digite números positivos para somar. Digite um número negativo para encerrar.");

        int numero = 0;

        // Enquanto o número for positivo, continua somando
        while (numero >= 0) {
            System.out.print("Digite um número: ");
            numero = scanner.nextInt();

            if (numero >= 0) {
                soma += numero;
            }
        }

        System.out.println("Soma dos números positivos digitados: " + soma);

        scanner.close();
    }
}
