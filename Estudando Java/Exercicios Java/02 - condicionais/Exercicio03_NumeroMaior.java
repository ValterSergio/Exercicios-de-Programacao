import java.util.Scanner;

public class Exercicio03_NumeroMaior {

    public static void main(String[] args) {
        // Cria o Scanner para ler entrada do usuário
        Scanner scanner = new Scanner(System.in);

        System.out.println("\n\tQual número é maior ? ");

        // Solicita o priimeiro número
        System.out.print("Digite o primeiro número: ");
        int numero1 = scanner.nextInt();

        // Solicita o segundo número
        System.out.print("Digite o segundo número: ");
        int numero2 = scanner.nextInt();

        // Verifica qual número é maior (ou se são iguais)
        if (numero1 > numero2) {
            System.out.println("O primeiro número é maior: " + numero1);
        } else if (numero2 > numero1) {
            System.out.println("O segundo número é maior: " + numero2);
        } else {
            System.out.println("Os dois números são iguais.");
        }

        // Fecha o scanner
        scanner.close();
    }
}
