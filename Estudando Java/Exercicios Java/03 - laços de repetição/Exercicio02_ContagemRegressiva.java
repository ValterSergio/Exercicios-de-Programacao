import java.util.Scanner;

public class Exercicio02_ContagemRegressiva {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Solicita o número inicial da contagem
        System.out.print("Digite o número inicial da contagem regressiva: ");
        int inicio = scanner.nextInt();

        // Faz a contagem regressiva até 0
        System.out.println("Contagem regressiva:");
        for (int i = inicio; i >= 0; i--) {
            System.out.println(i);
        }

        // Exibe mensagem final
        System.out.println("🚀 Lançamento!");

        scanner.close();
    }
}
