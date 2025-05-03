import java.util.Scanner;

public class exercicio_1 {

    public static void main(String[] args) {
        // vetor de string
        String[] nomesSimples = new String[5];

        Scanner scanner = new Scanner(System.in);

        for (int i = 0; i < 5; i++){
            System.out.print("Digite um nome: ");
            nomesSimples[i] = scanner.nextLine();
        }

        scanner.close();
        
        System.out.print("Nomes no vetor: { ");
        for (int i = 0; i < nomesSimples.length; i++) {
            System.out.printf(" %s ", nomesSimples[i]);
        }
        System.out.print("} ");
    }
}