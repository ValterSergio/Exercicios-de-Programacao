import java.util.Scanner;

public class exercicio_7 {
    public static void main(String[] args) {
        
        //vetor
        int[] vetor = new int[12];

        //scanner
        Scanner scanner = new Scanner(System.in);

        // contadores
        int positivos = 0;
        int negativos = 0;
        int zeros = 0;

        for (int i = 0; i < vetor.length; i++) {
            System.out.print("Digite um número: ");
            vetor[i] = scanner.nextInt();
            scanner.nextLine();

            if (vetor[i] == 0) {
                zeros++;
            } else if (vetor[i] < 0) {
                negativos++;
            } else {
                positivos++;
            }
        }
    
        
        // trecho para teste real
        System.out.print("Numeros digitados { ");
        for (int i = 0; i < vetor.length; i++) {
            System.out.printf(" %d ", vetor[i]);
        }
        System.out.print("}\n");

        System.out.println("Total de Numeros positivos: " + positivos);
        System.out.println("Total de Numeros negativos: " + negativos);
        System.out.println("Total de Numeros zero: " + zeros);

        scanner.close();
    }
}
