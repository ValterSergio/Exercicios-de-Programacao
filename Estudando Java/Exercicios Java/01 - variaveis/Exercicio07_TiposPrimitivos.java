public class Exercicio07_TiposPrimitivos {

    public static void main(String[] args) {

        // Tipos inteiros
        byte tipoByte = 120;              // ocupa 1 byte (–128 a 127)
        short tipoShort = 32000;          // ocupa 2 bytes
        int tipoInt = 1500000000;         // ocupa 4 bytes (valor mais comum)
        long tipoLong = 90000000000L;     // ocupa 8 bytes (necessita 'L' no final)

        // Tipos decimais
        float tipoFloat = 3.14f;          // ocupa 4 bytes (necessita 'f' no final)
        double tipoDouble = 3.1415926535; // ocupa 8 bytes (mais preciso)

        // Tipo caractere
        char tipoChar = 'A';              // armazena apenas um caractere

        // Tipo lógico
        boolean tipoBoolean = true;       // true ou false

        // Impressão dos valores
        System.out.println("byte: " + tipoByte);
        System.out.println("short: " + tipoShort);
        System.out.println("int: " + tipoInt);
        System.out.println("long: " + tipoLong);
        System.out.println("float: " + tipoFloat);
        System.out.println("double: " + tipoDouble);
        System.out.println("char: " + tipoChar);
        System.out.println("boolean: " + tipoBoolean);
    }
}
