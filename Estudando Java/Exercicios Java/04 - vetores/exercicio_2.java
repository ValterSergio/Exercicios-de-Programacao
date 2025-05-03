import java.util.Scanner;

public class exercicio_2 {
    public static void main(String[] args) {
        // vetor de Números inteiros
        int[] vetor = new int[10];

        // scanner
        Scanner scanner = new Scanner(System.in);

        // contador
        int cont = 0;
        double media;

        // preencher vetor
        for (int i = 0; i < vetor.length; i++) {

            // obter numero do usuario
            System.out.print("Digite um número: ");   
            vetor[i] = scanner.nextInt();
            scanner.nextLine();

            cont += vetor[i];
        }
        
        // exibindo vetor
        System.out.print("\nNumeros escolhidos: {");
        for (int i = 0; i < vetor.length; i++) {
            System.out.printf(" %d ", vetor[i]);
        }
        System.out.print("}\n");
        
        // exibindo resultado
        System.out.println("Soma de todos os valores: " + cont);
        media = (double) cont / (double) vetor.length;
        System.out.println("Média dos elementos: " + media);

        // fechando scanner
        scanner.close();
    }
}
