import java.util.Scanner;

public class Exercicio20_ContadorMaioresIdade {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Quantas pessoas você quer analisar? ");
        int totalPessoas = scanner.nextInt();

        int contador = 1;
        int maiores = 0;
        int menores = 0;

        // Repete para cada pessoa
        while (contador <= totalPessoas) {
            System.out.print("Digite a idade da pessoa " + contador + ": ");
            int idade = scanner.nextInt();

            if (idade >= 18) {
                maiores++;
            } else {
                menores++;
            }

            contador++;
        }

        System.out.println("\nTotal de maiores de idade: " + maiores);
        System.out.println("Total de menores de idade: " + menores);

        scanner.close();
    }
}
