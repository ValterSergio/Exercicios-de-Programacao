public class DiferencaSomaDosQuadradosEOQuadradoDaSoma {
    public static void main(String[] args) {

        int n = 100;
        int soma = n * (n + 1) / 2;
        int quadrado_da_soma = soma * soma;
        int soma_dos_quadrados = n * (n +1) * (2 * n + 1) / 6;
        int diferenca = quadrado_da_soma - soma_dos_quadrados;

        System.out.println("A diferença: " + diferenca);
    }
}
