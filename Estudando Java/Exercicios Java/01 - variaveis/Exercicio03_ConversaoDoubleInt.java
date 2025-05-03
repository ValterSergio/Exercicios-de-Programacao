import java.util.Scanner;

public class Exercicio03_ConversaoDoubleInt {

    public static void main(String[] args) {
        // Cria o Scanner para entrada do usuário
        Scanner scanner = new Scanner(System.in);

        // Solicita um número com casas decimais
        System.out.print("Digite um número decimal (ex: 5.75): ");
        double numeroDecimal = scanner.nextDouble();

        // Converte o número double para int (casting explícito)
        int numeroInteiro = (int) numeroDecimal;

        // Exibe os dois valores
        System.out.println("Número original (double): " + numeroDecimal);
        System.out.println("Número convertido para inteiro: " + numeroInteiro);

        // Fecha o scanner
        scanner.close();
    }
}
