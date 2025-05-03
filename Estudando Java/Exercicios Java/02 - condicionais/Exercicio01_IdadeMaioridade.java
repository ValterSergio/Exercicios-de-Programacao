import java.util.Scanner;

public class Exercicio01_IdadeMaioridade {

    public static void main(String[] args) {
        // Cria o Scanner para entrada do usuário
        Scanner scanner = new Scanner(System.in);

        // Solicita a idade
        System.out.print("Digite sua idade: ");
        int idade = scanner.nextInt();

        // Verifica se é maior de idade
        if (idade >= 18) {
            System.out.println("Você é maior de idade.");
        } else {
            System.out.println("Você é menor de idade.");
        }

        // Fecha o scanner
        scanner.close();
    }
}
