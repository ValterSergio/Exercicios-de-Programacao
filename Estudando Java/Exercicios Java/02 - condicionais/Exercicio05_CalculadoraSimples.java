import java.util.Scanner;

public class Exercicio05_CalculadoraSimples {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Solicita o primeiro número
        System.out.print("Digite o primeiro número: ");
        double numero1 = scanner.nextDouble();

        // Solicita o segundo número
        System.out.print("Digite o segundo número: ");
        double numero2 = scanner.nextDouble();

        // Solicita a operação desejada
        System.out.print("Digite a operação (+, -, *, /): ");
        char operador = scanner.next().charAt(0); // lê o primeiro caractere

        // Executa a operação de acordo com o operador informado
        if (operador == '+') {
            System.out.println("Resultado: " + (numero1 + numero2));
        } else if (operador == '-') {
            System.out.println("Resultado: " + (numero1 - numero2));
        } else if (operador == '*') {
            System.out.println("Resultado: " + (numero1 * numero2));
        } else if (operador == '/') {
            if (numero2 != 0) {
                System.out.println("Resultado: " + (numero1 / numero2));
            } else {
                System.out.println("Erro: divisão por zero não é permitida!");
            }
        } else {
            System.out.println("Operador inválido!");
        }

        // Fecha o scanner
        scanner.close();
    }
}
