/*
Cada novo termo na sequência de Fibonacci é gerado pela 
adição dos dois termos anteriores. Começando com 1 e 2, os 
primeiros 10 termos serão:

    1, 2, 3, 5, 8, 13, 21, 34, 55, 89

Considerando os termos na sequência de Fibonacci cujos 
valores não excedem 4 milhões, encontre a soma dos termos de 
valor par.
*/


public class NumerosParesDeFibonacci {
    public static void main(String[] args) {
        
        int primeiro = 0;
        int segundo = 1;
        int somar = 0;

        while (true){
            int fibo = primeiro + segundo;
            primeiro = segundo;
            segundo = fibo;
            
            if (fibo >= 4000000){
                break;
            }

            if (fibo % 2 == 0){
                somar += fibo;
            }
        }
        System.out.println("A soma dos números pares: " + somar);
    }
}
