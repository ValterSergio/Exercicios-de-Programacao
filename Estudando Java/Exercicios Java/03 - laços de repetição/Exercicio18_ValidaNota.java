import java.util.Scanner;

public class Exercicio18_ValidaNota {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        double nota;

        System.out.println("Digite uma nota entre 0 e 10:");

        // Lê a nota
        nota = scanner.nextDouble();

        // Enquanto a nota for inválida, continua pedindo
        while (nota < 0 || nota > 10) {
            System.out.println("Nota inválida! Tente novamente.");
            System.out.print("Digite uma nota entre 0 e 10: ");
            nota = scanner.nextDouble();
        }

        System.out.println("Nota registrada com sucesso: " + nota);

        scanner.close();
    }
}
