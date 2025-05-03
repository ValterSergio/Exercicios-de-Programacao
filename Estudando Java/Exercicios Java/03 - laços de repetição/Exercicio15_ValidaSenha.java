import java.util.Scanner;

public class Exercicio15_ValidaSenha {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int tentativas = 5;

        final String SENHA_CORRETA = "valter";
        String senhaDigitada;

        System.out.println("Bem-vindo! Para acessar o sistema, digite a senha correta.");

        // Continua pedindo até acertar
        do {
            System.out.print("Digite a senha: ");
            senhaDigitada = scanner.nextLine();

            if (!senhaDigitada.equals(SENHA_CORRETA)) {
                System.out.println("Senha incorreta. Tente novamente.\n");
                tentativas--;
                if (tentativas > 0){
                    System.out.println("Tentativas restante: " + tentativas);
                
                } else {
                    System.out.println("Tentativas bloqueadas");
                    System.exit(0);
                }
            } else {

                System.out.println("Acesso permitido. Bem-vindo ao sistema!");
            }

        } while (!senhaDigitada.equals(SENHA_CORRETA));


        scanner.close();
    }
}
