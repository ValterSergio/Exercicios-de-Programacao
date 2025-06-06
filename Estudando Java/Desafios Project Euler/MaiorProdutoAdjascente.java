/*
Problema 8 do Project Euler:

Dado um número de 1000 dígitos, o objetivo é encontrar o maior produto possível
de 13 dígitos consecutivos.

A estratégia consiste em percorrer o número, separando todas as combinações possíveis
de 13 dígitos, calcular o produto de cada uma e manter o maior valor encontrado.

Link do desafio: https://projecteuler.net/problem=8
*/

public class MaiorProdutoAdjascente {
    public static void main(String[] args) {
        String numeroGrande =
            "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843" +
            "8586156078911294949545950173795833195285320880551112540698747158523863050715693290963295227443043557" +
            "6689664895044524452316173185640309871112172238311362229893423380308135336276614282806444486645238749" +
            "3035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776" +
            "6572733300105336788122023542180975125454059475224352584907711670556013604839586446706324415722155397" +
            "5369781797784617406495514929086256932197846862248283972241375657056057490261407972968652414535100474" +
            "8216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586" +
            "1786645835912456652947654568284891288314260769004224219022671055626321111109370544217506941658960408" +
            "0719840385096245544436298123098787992724428490918884580156166097919133875499200524063689912560717606" +
            "0588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450";

        int tamanhoTotal = numeroGrande.length();
        int tamanhoSequencia = 13;

        long maiorProduto = 0;
        String melhorSequencia = "";

        for (int posicao = 0; posicao < tamanhoTotal; posicao++) {
            for (int deslocamento = 0; deslocamento < tamanhoTotal - posicao - 1; deslocamento++) {
                if (deslocamento + tamanhoSequencia > tamanhoTotal) {
                    break;
                }

                String sequencia = numeroGrande.substring(deslocamento, deslocamento + tamanhoSequencia);
                long produtoAtual = 1;

                for (char c : sequencia.toCharArray()) {
                    int digito = Character.getNumericValue(c);
                    produtoAtual *= digito;
                }

                if (produtoAtual > maiorProduto) {
                    maiorProduto = produtoAtual;
                    melhorSequencia = sequencia;
                }
            }
        }

        System.out.println("Maior produto encontrado: " + maiorProduto);
        System.out.println("Sequência correspondente: " + melhorSequencia);
    }
}
