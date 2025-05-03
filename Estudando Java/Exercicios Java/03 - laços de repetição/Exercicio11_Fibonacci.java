import java.util.Scanner;

public class Exercicio11_Fibonacci {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Quantos termos da sequência de Fibonacci você quer ver? ");
        int termos = scanner.nextInt();

        int primeiro = 0;
        int segundo = 1;

        System.out.print("Sequência de Fibonacci: ");

        for (int i = 0; i < termos; i++) {
            System.out.print(primeiro + " ");

            // Próximo número da sequência é a soma dos dois anteriores
            int proximo = primeiro + segundo;
            primeiro = segundo;
            segundo = proximo;
        }

        scanner.close();
    }
}
