import java.util.Scanner;

public class exercicio_6 {
    
    public static void main(String[] args) {
        
        // criar vetor
        int[] vetor = new int[6];

        // iniciar scanner
        Scanner scanner = new Scanner(System.in);

        // variaveis de comparação
        int maiorValor = Integer.MIN_VALUE;
        int menorValor = Integer.MAX_VALUE;

        for (int i = 0; i < vetor.length; i++) {
            System.out.print("Digite um numero: ");
            vetor[i] = scanner.nextInt();
            scanner.nextLine(); // limpar scanner

            if (vetor[i] >= maiorValor) {
                maiorValor = vetor[i];
            }
            if (vetor[i] < menorValor) {
                menorValor = vetor[i];
            }
        }

        // trecho para teste real
        System.out.print("Numeros digitados { ");
        for (int i = 0; i < vetor.length; i++) {
            System.out.printf(" %d ", vetor[i]);
        }
        System.out.print("}\n");

        // saida
        System.out.println("Maior numero: " + maiorValor);
        System.out.println("Menor numero: " + menorValor);

        // fechar scanner
        scanner.close();
    }
}
