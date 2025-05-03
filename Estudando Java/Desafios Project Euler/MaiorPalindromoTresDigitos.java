/* 
Um número palíndromo é aquele que pode ser lido da mesma forma em ambos os sentidos.
O maior palíndromo formado pelo produto de dois números de 2 dígitos é 9009 = 91 × 99.
Encontre o maior palíndromo formado pelo produto de dois números de 3 dígitos.
*/

public class MaiorPalindromoTresDigitos {
    public static String inverterString(String str){

        // Converter a String para um array
        char[] caracteres = str.toCharArray();

        // definir inicio e fim
        int inicio = 0;
        int fim = caracteres.length - 1;

        while (inicio < fim) {
            
            char temp = caracteres[inicio];
            caracteres[inicio] = caracteres[fim];
            caracteres[fim] = temp;
            inicio++;
            fim--;
        }
        return new String(caracteres);

    }
    
    public static void main(String[] args) {

        int num = 100;
        int mult = 1;
        int palíndromo = 0;

        while (num <= 999) {
            mult = num;
            while (mult <= 999) {
                String produto = String.valueOf(num * mult);
                String inverterProduto = inverterString(produto);
                if (inverterProduto.equals(produto)){
                    int TempPalindromo = Integer.parseInt(produto);
                    if (TempPalindromo > palíndromo){
                        palíndromo = TempPalindromo;
                    }
                

                }
            mult++;
            }
        num++;
        }
    System.out.println("O maior palindromo de 3 digitos: " + palíndromo);
    }
}
