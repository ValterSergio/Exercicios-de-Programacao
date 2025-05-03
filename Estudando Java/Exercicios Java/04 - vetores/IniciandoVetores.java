/*
 * Vetores em java é  uma estrutura de dados para armazenar 
 * valores de um mesmo tipo de dado.
 * Cada valor no vetor é armazenado em posições numeradas
 * todo vetor começa pela posição 0(zero), essa caracteristica
 * de indexação permite o facil acesso aos elementos dos 
 * vetores
 * além da organização dos dados e do acesso eficiente, os 
 * vetores são a base para a criação de outras estruturas de 
 * dados como matrizes e listas
 */

public class IniciandoVetores {
/*
    * Existem algumas regras para declarar um vetor
    * 
    * Precisamos definir o tipo de dado: String, int, double 
    * e etc.
    * Envolver o tipo com colchetes e nomear o vetor
    * exemplo: tipo[] nomeVetor;
    *
    * Existem também algumas regras para Iniciar o vetor
    * 
    * Precisamos definir o tamanho do vetor e usar a palavra 
    * chave new seguido do tipo com o total de elementos que 
    * deve ser reservado para o vetor.
    *
    * O tamanho do vetor é fixo após ele ser definido 
    * exemplo: tipo[] nomeVetor = new tipo[tamanho reservado]
    * 
    * podemos adicionar ou não os valores iniciais (opcional)
    * para definir os valores diretamente usamos chaves {}
    * exemplo: tipo[] nomeVetor = {valor1, valor2, ...}
    * 
    */
    public static void main(String[] args) {
        
        // declarar um vetor com 5 numeros inteiros
        int[] numeros = new int[5];
        
        // usando indexação para preencher os valores
        numeros[0] = 1;
        numeros[1] = 2;
        numeros[2] = 3;
        numeros[3] = 4;
        numeros[4] = 5;
        
        System.out.println("Exibindo Posição e valores definidos");
        // vamos exibir esse vetor
        for (int i = 0; i < numeros.length; i++){
            System.out.printf("Posição: %d   Valor: %d\n", i, numeros[i]);
        }

        System.out.println("\nAlterando os valores pela posição");
        // podemos alterar os valores do valor usando a posição

        // vamos modificar os valores pela posição dos valores 
        for (int i = 4; i >= 0; i--){
            numeros[i] = 5 - i;
            System.out.printf("Posição: %d     Valor: %d\n", i, numeros[i]);
        }

        // podemos obter o tamanho do vetor usando lenght
        System.out.printf("\nO vetor tem %d elementos.\n", numeros.length);

        System.out.print("\nDeclarando vetor de strings");
        
        // vamos declarar um vetor de strings
        String[] nomes = new String[5];
        
        nomes[0] = "valter";
        nomes[1] = "wanderley";
        nomes[2] = "wictor";
        nomes[3] = "wando";
        nomes[4] = "wagner";

        // para vetores de string podemos usar o "for-each"
        // não é necessario um contador para esse caso, sendo 
        // mais facil de escrever
        for (String i : nomes){
            System.out.printf("\nNome: %s", i);
        }
    }
}