import java.util.Scanner;

public class exercicio_5 {
    public static void main(String[] args) {
        // vetor de Números inteiros
        int[] vetor = new int[10];

        // scanner
        Scanner scanner = new Scanner(System.in);

        // preencher vetor
        for (int i = vetor.length - 1; i >= 0; i--) {

            // obter numero do usuario
            System.out.print("Digite um número: ");   
            vetor[i] = scanner.nextInt();
            scanner.nextLine();
        }
        
        // exibindo vetor
        System.out.print("\nNumeros invertidos: {");
        for (int i = 0; i < vetor.length; i++) {
            System.out.printf(" %d ", vetor[i]);
        }
        System.out.print("}\n");
        
        // fechar scanner
        scanner.close();
    }
}