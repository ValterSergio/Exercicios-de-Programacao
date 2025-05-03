import java.util.Scanner;

public class Exercicio08_SenhaCorreta {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        final String SENHA_CORRETA = "1234"; // Constante com a senha correta
        String senhaDigitada;

        // Repete até o usuário digitar a senha correta
        do {
            System.out.print("Digite a senha: ");
            senhaDigitada = scanner.nextLine();

            if (!senhaDigitada.equals(SENHA_CORRETA)) {
                System.out.println("Senha incorreta. Tente novamente.");
            }

        } while (!senhaDigitada.equals(SENHA_CORRETA));

        System.out.println("Acesso permitido!");

        scanner.close();
    }
}
