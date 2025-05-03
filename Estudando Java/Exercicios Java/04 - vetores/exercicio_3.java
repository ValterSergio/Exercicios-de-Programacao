import java.util.Scanner;

public class exercicio_3 {
    // verificar se é par
    public static boolean enumeroPar(int num){
        if (num % 2 == 0){
            return true;
        } else {
            return false;
        }
    }
    
    public static void main(String[] args) {
        // vetor de Números inteiros
        int[] vetor = new int[10];

        // scanner
        Scanner scanner = new Scanner(System.in);

        // contador
        int totalPares = 0;
        int totalImpares = 0;

        // preencher vetor
        for (int i = 0; i < vetor.length; i++) {

            // obter numero do usuario
            System.out.print("Digite um número: ");   
            vetor[i] = scanner.nextInt();
            scanner.nextLine();
            if (enumeroPar(vetor[i])) {
                totalPares++;
            } else {
                totalImpares++;
            }


        }
        
        // exibindo vetor
        System.out.print("\nNumeros escolhidos = {");
        for (int i = 0; i < vetor.length; i++) {
            String mensagem;
            
            if (enumeroPar(vetor[i])){
                mensagem = "Par";
            } else {
            mensagem = "Impar";
            }

            System.out.printf("\n    '%d': %s, ", vetor[i], mensagem);
        }
        System.out.print("\n }\n");
        System.out.println("Existem " + totalPares + " Numeros Pares");
        System.out.println("\nExistem " + totalImpares + " Numeros Impares");


        // fechando scanner
        scanner.close();
    }
}
