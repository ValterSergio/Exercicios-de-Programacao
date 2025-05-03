import java.util.Scanner;

public class Exercicio10_NumeroPrimo {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Digite um número inteiro positivo: ");
        int numero = scanner.nextInt();

        boolean ehPrimo = true;

        // Todo número menor ou igual a 1 não é primo
        if (numero <= 1) {
            ehPrimo = false;
        } else {
            // Verifica se o número tem divisores além de 1 e ele mesmo
            for (int i = 2; i < numero; i++) {
                if (numero % i == 0) {
                    ehPrimo = false;
                    break;
                }
            }
        }

        // Exibe o resultado
        if (ehPrimo) {
            System.out.println(numero + " é um número primo.");
        } else {
            System.out.println(numero + " NÃO é um número primo.");
        }

        scanner.close();
    }
}
