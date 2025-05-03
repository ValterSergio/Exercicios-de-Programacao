import java.util.Scanner;

public class Exercicio19_MediaNotas {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Quantas notas você quer digitar? ");
        int totalNotas = scanner.nextInt();

        int contador = 1;
        double soma = 0;

        // Enquanto não atingir o total desejado, continua pedindo notas
        while (contador <= totalNotas) {
            System.out.print("Digite a nota " + contador + ": ");
            double nota = scanner.nextDouble();

            // validação da nota
            if (nota < 0 || nota > 10) {
                System.out.println("Nota inválida! Digite entre 0 e 10.");
                continue; // volta pro começo do laço sem aumentar o contador
            }

            soma += nota;
            contador++;
        }

        double media = soma / totalNotas;

        System.out.println("\nMédia das notas: " + media);

        scanner.close();
    }
}
