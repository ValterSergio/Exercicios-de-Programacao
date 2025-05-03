import java.util.Scanner;

public class Exercicio09_MediaNotas {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Quantas notas deseja informar? ");
        int quantidadeNotas = scanner.nextInt();

        double soma = 0;

        // Loop para ler as notas e somar
        for (int i = 1; i <= quantidadeNotas; i++) {
            System.out.print("Digite a nota " + i + ": ");
            double nota = scanner.nextDouble();
            soma += nota;
        }

        // Calcula a média
        double media = soma / quantidadeNotas;

        System.out.println("A média das notas é: " + media);

        scanner.close();
    }
}
