public class MenorMultiplo {
    
    //algoritmo de euclides
    public static int mdc(int a, int b){
        while (b != 0){
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }

    // calcular mmc
    public static int mmc(int a, int b){
        return a * (b / mdc(a, b));

    }

    // obter o menor multiplo de 1 a 20
    public static void main(String[] args) {
        int resultado = 1;

        for (int i = 2; i <= 20; i++){
            resultado = mmc(resultado, i);
        }
        System.out.println("O menor numero divisivel de 1 a 20 é :" + resultado);
    }
}
