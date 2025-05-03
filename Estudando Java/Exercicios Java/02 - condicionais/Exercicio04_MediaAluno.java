import java.util.Scanner;

public class Exercicio04_MediaAluno {

    public static void main(String[] args) {
        // Scanner para ler entrada do usuário
        Scanner scanner = new Scanner(System.in);

        // Solicita a primeira nota
        System.out.print("Digite a primeira nota: ");
        double nota1 = scanner.nextDouble();

        // Solicita a segunda nota
        System.out.print("Digite a segunda nota: ");
        double nota2 = scanner.nextDouble();

        // Calcula a média
        double media = (nota1 + nota2) / 2;

        // Exibe a média
        System.out.println("Média do aluno: " + media);

        // Verifica a situação do aluno
        if (media >= 7) {
            System.out.println("Situação: Aprovado");
        } else if (media >= 5) {
            System.out.println("Situação: Recuperação ");
        } else {
            System.out.println("Situação: Reprovado");
        }

        // Fecha o scanner
        scanner.close();
    }
}
