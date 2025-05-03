import java.util.Scanner;

public class Exercicio01_Tabuada {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Solicita o número para gerar a tabuada
        System.out.print("Digite um número para ver a tabuada: ");
        int numero = scanner.nextInt();

        // Laço que vai de 1 a 10 para calcular a tabuada
        System.out.println("Tabuada do " + numero + ":");
        for (int i = 1; i <= 10; i++) {
            int resultado = numero * i;
            System.out.println(numero + " x " + i + " = " + resultado);
        }

        scanner.close();
    }
}
