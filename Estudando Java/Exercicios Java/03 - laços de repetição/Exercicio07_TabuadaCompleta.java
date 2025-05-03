public class Exercicio07_TabuadaCompleta {

    public static void main(String[] args) {

        // Loop externo: controla o número base da tabuada (1 a 10)
        for (int i = 1; i <= 10; i++) {
            System.out.println("Tabuada do " + i + ":");

            // Loop interno: multiplica o número base pelos valores de 1 a 10
            for (int j = 1; j <= 10; j++) {
                int resultado = i * j;
                System.out.println(i + " x " + j + " = " + resultado);
            }

            System.out.println(); // Linha em branco entre as tabuadas
        }
    }
}
