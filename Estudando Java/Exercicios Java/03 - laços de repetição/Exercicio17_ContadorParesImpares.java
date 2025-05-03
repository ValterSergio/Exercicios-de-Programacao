import java.util.Scanner;

public class Exercicio17_ContadorParesImpares {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int numero;
        int pares = 0;
        int impares = 0;

        System.out.println("Digite números inteiros. Digite 0 para encerrar.");

        // Pede o primeiro número
        System.out.print("Número: ");
        numero = scanner.nextInt();

        // Continua até digitar 0
        while (numero != 0) {
            if (numero % 2 == 0) {
                pares++;
            } else {
                impares++;
            }

            System.out.print("Número: ");
            numero = scanner.nextInt();
        }

        System.out.println("\nTotal de números pares: " + pares);
        System.out.println("Total de números ímpares: " + impares);

        scanner.close();
    }
}
