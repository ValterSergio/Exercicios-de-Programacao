import java.util.Scanner;

public class Exercicio12_ContadorParImpar {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Quantos números deseja digitar? ");
        int quantidade = scanner.nextInt();

        int pares = 0;
        int impares = 0;

        for (int i = 1; i <= quantidade; i++) {
            System.out.print("Digite o " + i + "º número: ");
            int numero = scanner.nextInt();

            if (numero % 2 == 0) {
                pares++;
            } else {
                impares++;
            }
        }

        System.out.println("\nTotal de números pares: " + pares);
        System.out.println("Total de números ímpares: " + impares);

        scanner.close();
    }
}
