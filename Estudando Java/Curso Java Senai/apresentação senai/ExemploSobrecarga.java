public class ExemploSobrecarga {
    public static void somar(int a, int b){
        int resultado = a + b;
        System.out.println("Resultado: " + resultado);
    }

    public static void somar(int... numeros){
        int resultado = 0;
        for (int i = 0; i < numeros.length; i++) {
            resultado += numeros[i];
        }
        System.out.println("Resultado: " + resultado);
    }

    public static void main(String[] args) {
        int a, b, c, d, e;
        a = 1;
        b = 2;
        c = 3;
        d = 4;
        e = 5;

        somar(a, b);
        somar(a, b, c, d, e);
        
    }
}
