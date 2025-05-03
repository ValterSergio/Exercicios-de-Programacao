// Os fatores primos de 13195 são 5, 7, 13 e 29.

// Qual é o maior fator primo do número 600851475143?


public class MaiorFatorPrimo {

    public static void main(String[] args) {
        
        long numero = 600851475143L;
        long fator = 2;
        long MaiorFatorPrimo = 0;

        while (numero > 1){
            if (numero % fator == 0){
                MaiorFatorPrimo = fator;
                numero = numero / fator;
            } else {
                fator++;
            }
        }
        System.out.println("O maior fator primo: " + MaiorFatorPrimo);
    }
    
}
