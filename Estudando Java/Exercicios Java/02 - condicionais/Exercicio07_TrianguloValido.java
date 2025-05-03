import java.util.Scanner;

public class Exercicio07_TrianguloValido {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Solicita os três lados
        System.out.print("Digite o valor do lado A: ");
        int ladoA = scanner.nextInt();

        System.out.print("Digite o valor do lado B: ");
        int ladoB = scanner.nextInt();

        System.out.print("Digite o valor do lado C: ");
        int ladoC = scanner.nextInt();

        // Verifica se os lados formam um triângulo válido
        if (ladoA < ladoB + ladoC && ladoB < ladoA + ladoC && ladoC < ladoA + ladoB) {
            System.out.println("Os lados formam um triângulo válido!");
        } else {
            System.out.println("Os lados NÃO formam um triângulo.");
        }

        // Fecha o scanner
        scanner.close();
    }
}
