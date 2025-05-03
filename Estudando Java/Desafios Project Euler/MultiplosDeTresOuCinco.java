/*
 * Se listarmos todos os números naturais abaixo de 10
 * que são múltiplos de 3 ou 5, nós teremos 3, 5, 6 e 9 e
 * a soma desses múltiplos é 23
 * 
 * Problema: Encontre a soma de todos os multiplos de 3 ou 5
 * abaixo de 1000
 */

public class MultiplosDeTresOuCinco {

    public static void main(String[] args) {
        int somar = 0;

        for (int i = 0; i < 1000; i++){
            if (i % 3 == 0 || i % 5 == 0){
                somar += i;
            }
        }

        System.out.println("A soma dos múltiplos de 3 ou 5 abaixo de 1000 é : " + somar);
    }
}