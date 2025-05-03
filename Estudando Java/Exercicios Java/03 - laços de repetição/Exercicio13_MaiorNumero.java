import java.util.Scanner;

public class Exercicio13_MaiorNumero {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Quantos números deseja digitar? ");
        int quantidade = scanner.nextInt();

        int maior = 0; // Começa com o menor valor possível

        for (int i = 1; i <= quantidade; i++) {
            System.out.print("Digite o " + i + "º número: ");
            int numero = scanner.nextInt();

            if (numero > maior) {
                maior = numero; // Atualiza se o número for maior que o anterior
            }
        }

        System.out.println("\nO maior número digitado foi: " + maior);

        scanner.close();
    }
}
