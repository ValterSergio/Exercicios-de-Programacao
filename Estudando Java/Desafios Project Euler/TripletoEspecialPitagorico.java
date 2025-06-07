/*
 * Desafio: Tripleto Pitagórico Especial
 *
 * Um tripleto pitagórico consiste em três números inteiros positivos a < b < c, tal que:
 *     a^2 + b^2 = c^2
 *
 * Existe exatamente um tripleto pitagórico para o qual:
 *     a + b + c = 1000
 *
 * Escreva um programa em Java que encontre o valor de a, b e c que satisfazem essa condição,
 * e imprima o produto a * b * c.
 */

public class TripletoEspecialPitagorico {
    public static void main(String[] args) {
        System.out.println("Procurando tripleto pitagórico...");
        
        for (int a = 1; a < 1000; a++) {
            for (int b = a + 1; b < 1000; b++) {
                int c = 1000 - a - b;
                if (a * a + b * b == c * c) {
                    System.out.println("Tripleto encontrado: a = " + a + " b = " + b + " c = " + c);
                    System.out.println("Produto de a x b x c: " + (a * b * c));
                    return; 
                }
            }
        }

        System.out.println("Nenhum tripleto encontrado.");
    }
}
