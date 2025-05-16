import java.util.Scanner;

public class CalculadoraVersaoUm {

    public static double somar(double a, double b) {
        return a + b;
    }

    public static double subtrair(double a, double b) {
        return a - b;
    }

    public static double dividir(double a, double b) {
        if (b == 0) {
            System.out.println("Não é possível dividir por zero. Resultado será considerado 0.");
            return 0;
        }
        return a / b;
    }

    public static double multiplicar(double a, double b){
        return a * b;
    }

    public static double obterNumero(Scanner scanner){
        System.out.print("Digite um número: ");
        double escolha = scanner.nextDouble();
        scanner.nextLine(); // consumir o enter
        return escolha;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int escolha;

        do {
            System.out.println("\n\t--- Bem-vindo à Calculadora ---");
            System.out.println("1 - Somar");
            System.out.println("2 - Subtrair");
            System.out.println("3 - Dividir");
            System.out.println("4 - Multiplicar");
            System.out.println("0 - Sair");
            System.out.print("Escolha uma opção: ");
            escolha = scanner.nextInt();
            scanner.nextLine(); // consumir o enter

            double a, b, resultado;

            switch (escolha) {
                case 1:
                    System.out.println("\tSomando...");
                    a = obterNumero(scanner);
                    b = obterNumero(scanner);
                    resultado = somar(a, b);
                    System.out.printf("Resultado: %.2f + %.2f = %.2f%n", a, b, resultado);
                    break;

                case 2:
                    System.out.println("\tSubtraindo...");
                    a = obterNumero(scanner);
                    b = obterNumero(scanner);
                    resultado = subtrair(a, b);
                    System.out.printf("Resultado: %.2f - %.2f = %.2f%n", a, b, resultado);
                    break;

                case 3:
                    System.out.println("\tDividindo...");
                    a = obterNumero(scanner);
                    b = obterNumero(scanner);
                    resultado = dividir(a, b);
                    System.out.printf("Resultado: %.2f / %.2f = %.2f%n", a, b, resultado);
                    break;

                case 4:
                    System.out.println("\tMultiplicando...");
                    a = obterNumero(scanner);
                    b = obterNumero(scanner);
                    resultado = multiplicar(a, b);
                    System.out.printf("Resultado: %.2f * %.2f = %.2f%n", a, b, resultado);
                    break;

                case 0:
                    System.out.println("Saindo da calculadora. Até logo!");
                    break;

                default:
                    System.out.println("Opção inválida. Tente novamente.");
                    break;
            }

        } while (escolha != 0);

        scanner.close();
    }
}
