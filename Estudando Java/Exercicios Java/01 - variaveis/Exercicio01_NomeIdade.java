import java.util.Scanner;

public class Exercicio01_NomeIdade {

    public static void main(String[] args) {

        // Uma saudação inicial
        System.out.println("\n\tOlá, seja bem-vindo !!!!\n");

        // Criando objeto Scanner para ler do teclado
        Scanner scanner = new Scanner(System.in);

        // Solicita o nome do usuário
        System.out.print("Digite seu nome: ");
        String nome = scanner.nextLine();

        // Solicita a idade do usuário
        System.out.print("Digite sua idade: ");
        int idade = scanner.nextInt();

        // Exibe mensagem com nome e idade
        System.out.println("Olá, " + nome + "! Você tem " + idade + " anos.");

        // Fecha o scanner
        scanner.close();
    }
}
