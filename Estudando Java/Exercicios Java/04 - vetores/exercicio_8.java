import java.util.Scanner;

public class exercicio_8 {
    public static void main(String[] args) {
                //vetor
        int[] vetor = new int[12];

        //scanner
        Scanner scanner = new Scanner(System.in);

        for (int i = 0; i < vetor.length; i++) {
            System.out.print("Digite um número: ");
            vetor[i] = scanner.nextInt();
            scanner.nextLine();
        }

        // exibir antes da troca
        
        // trecho para teste real
        System.out.print("Numeros digitados { ");
        for (int i = 0; i < vetor.length; i++) {
            System.out.printf(" %d ", vetor[i]);
        }
        System.out.print("}\n");


        System.out.print("Digite a posição que trocar: " );
        int posicaoParaTrocar = scanner.nextInt();
        scanner.nextLine();
        
        System.out.print("Digite a nova posição: ");
        int novaPosicao = scanner.nextInt();
        scanner.nextLine();

        // validar intervalo de posição
        if (posicaoParaTrocar < 0 || posicaoParaTrocar >= vetor.length ||
        novaPosicao < 0 || novaPosicao >= vetor.length) {
        System.out.println("Posições inválidas. As posições devem estar entre 0 e " + (vetor.length - 1));
        System.out.println("Troca não realizada.");
    } else {
        // realizar troca
        int troca = vetor[posicaoParaTrocar];
        vetor[posicaoParaTrocar] = vetor[novaPosicao];
        vetor[novaPosicao] = troca;
        
        // exibir depois da troca
        System.out.print("Numeros digitados { ");
        for (int i = 0; i < vetor.length; i++) {
            System.out.printf(" %d ", vetor[i]);
        }
        System.out.print("}\n");
    }
        scanner.close();
    }
}
