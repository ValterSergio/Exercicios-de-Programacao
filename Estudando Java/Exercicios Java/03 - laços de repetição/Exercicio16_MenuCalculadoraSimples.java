import java.util.Scanner;

public class Exercicio16_MenuCalculadoraSimples {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // variavel de controle
        int opcao = 1;

        while (opcao != 0) {
            System.out.println("\n=== MENU CALCULADORA ===");
            System.out.println("1 - Somar dois números");
            System.out.println("2 - Subtrair dois números");
            System.out.println("0 - Sair");
            System.out.print("Escolha uma opção: ");
            opcao = scanner.nextInt();

            if (opcao == 1) {
                System.out.print("Digite o primeiro número: ");
                int n1 = scanner.nextInt();
                System.out.print("Digite o segundo número: ");
                int n2 = scanner.nextInt();
                int soma = n1 + n2;
                System.out.println("Resultado da soma: " + soma);

            } else if (opcao == 2) {
                System.out.print("Digite o primeiro número: ");
                int n1 = scanner.nextInt();
                System.out.print("Digite o segundo número: ");
                int n2 = scanner.nextInt();
                int subtracao = n1 - n2;
                System.out.println("Resultado da subtração: " + subtracao);

            } else if (opcao == 0) {
                System.out.println("Saindo... Obrigado por usar a calculadora!");
            } else {
                System.out.println("Opção inválida. Tente novamente.");
            }
        }

        scanner.close();
    }
}
