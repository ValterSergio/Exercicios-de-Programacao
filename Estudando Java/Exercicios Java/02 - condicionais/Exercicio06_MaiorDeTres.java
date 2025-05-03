import java.util.Scanner;

public class Exercicio06_MaiorDeTres {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Solicita os três números ao usuário
        System.out.print("Digite o primeiro número: ");
        int numero1 = scanner.nextInt();

        System.out.print("Digite o segundo número: ");
        int numero2 = scanner.nextInt();

        System.out.print("Digite o terceiro número: ");
        int numero3 = scanner.nextInt();

        // Verifica qual é o maior número
        if (numero1 > numero2 && numero1 > numero3) {
            System.out.println("O maior número é: " + numero1);
        } else if (numero2 > numero1 && numero2 > numero3) {
            System.out.println("O maior número é: " + numero2);
        } else if (numero3 > numero1 && numero3 > numero2) {
            System.out.println("O maior número é: " + numero3);
        } else {
            System.out.println("Existe pelo menos dois números iguais ou todos são iguais.");
        }

        // Fecha o scanner
        scanner.close();
    }
}
