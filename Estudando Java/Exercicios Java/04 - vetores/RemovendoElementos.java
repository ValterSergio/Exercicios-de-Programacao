/*
 * Em java não é possivel remover diretamente um elemento de 
 * um vetor, porque o tamanho deles são fixos
 * mas existem algumas maneiras de contornar isso
 */

public class RemovendoElementos {
    public static void main(String[] args) {
        // criando vetor
        int[] numeros = new int[10];

        System.out.println("Criando Vetor inicial");
        // preenchendo vetor
        for (int i = 0; i < 10; i++){
            numeros[i] = i * i;
            System.out.printf("\n| Posição: %d | Valor: %d |", i, numeros[i]);
        }
        System.out.println();
        System.out.println("\nAlterando Valores");
        System.out.println();

        // primeiro podemos substituir o valor por um valor que represente vazio
        // temos na posição 7 o numero 49
        System.out.printf("Posição: %d   Valor: %d", 7, numeros[7]);
        
        // vamos substituir ele por um numero abaixo de zero
        numeros[7] = -1;
        System.out.printf("\nPosição: %d   Valor: %d", 7, numeros[7]);
        System.out.println();
        System.out.println("\nRemovendo Valores");
        System.out.println();

        // ou criamos um novo vetor
        // vamos supor que queremos remover 25
        int removerValor = 25;

        // precisamos definir um novo tamanho e remover o espaço resevado
        int novoTamanho = numeros.length - 1;
        
        // iniciamos um novo vetor para guardar os items que queremos
        int[] removerNumeros = new int[novoTamanho];

        // criamos um marcador de indice para evitar erros de indexação
        int indice = 0;

        // percorremos o vetor original
        for (int i = 0; i < numeros.length; i++){

            // verificamos se o numero atual é diferente do que queremos remover
            if (numeros[i] != removerValor){
                removerNumeros[indice] = numeros[i];
                indice++;
            }
        }

        // vamos exibir o novo vetor e procurar pelo numero 25
        for (int i = 0; i < removerNumeros.length; i++){
            System.out.printf("| Posição: %d | Valor: %d|\n", i, removerNumeros[i]);
        }
    }
}
