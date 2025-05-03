import java.util.Scanner;

public class Exercicio04_Asteriscos {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Pede a quantidade de asteriscos que o usuário quer exibir
        System.out.print("Digite um número: ");
        int quantidade = scanner.nextInt();

        // Imprime asteriscos em uma única linha
        System.out.print("Resultado: ");
        for (int i = 1; i <= quantidade; i++) {
            System.out.print("*");
        }

        System.out.println(); // Quebra de linha no final

        scanner.close();
    }
}
