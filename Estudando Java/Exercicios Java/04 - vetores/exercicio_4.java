import java.util.Scanner;

public class exercicio_4 {

    public static void main(String[] args) {
        
        // iniciar vetor
        int[] vetor = new int[8];
        
        // variavel de busca
        int buscar;
        int posicao = 0;
        boolean estaPresente = false;

        // scanner
        Scanner scanner = new Scanner(System.in);


        // preencher vetor
        for (int i = 0; i < vetor.length; i++) {

            // obter numero do usuario
            System.out.print("Digite um número: ");   
            vetor[i] = scanner.nextInt();
            scanner.nextLine();
        }

        // obter numero de busca
        System.out.print("Digite o numero para buscar: ");
        buscar = scanner.nextInt();

        for (int i = 0; i < vetor.length; i++) {
            if (buscar == vetor[i]) {
               estaPresente = true;
               posicao = i;
               break;
            }
        }

        if (estaPresente) {
            System.out.printf("Número encontrado: %d\n", buscar);
            System.out.printf("Posição: %d", posicao);
        } else {
            System.out.println("Numero " + buscar + " não está na lista");
        }
        scanner.close();
    }
}