import java.util.Scanner;

public class Exercicio04_AreaRetangulo {

    public static void main(String[] args) {
        // Cria o Scanner para entrada do usuário
        Scanner scanner = new Scanner(System.in);

        // Solicita a base do retângulo
        System.out.print("Digite a base do retângulo (em metros): ");
        double base = scanner.nextDouble();

        // Solicita a altura do retângulo
        System.out.print("Digite a altura do retângulo (em metros): ");
        double altura = scanner.nextDouble();

        // Calcula a área do retângulo
        double area = base * altura;

        // Exibe o resultado
        System.out.println("A área do retângulo é: " + area + " m²");

        // Fecha o scanner
        scanner.close();
    }
}
