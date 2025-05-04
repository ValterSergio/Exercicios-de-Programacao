public class DesenvolverUmProblemaParteDois {

    public static void exibirVetor(int[] vetor){
        int hora = vetor[2], minuto = vetor[1], segundos = vetor[0];
        System.out.printf("Tempo de Viagem\nHoras: %d\nMinutos: %d\nsegundos: %d", hora, minuto, segundos);
    }

    public static int arredondarValores(double valor){
        return (int) Math.round(valor);
    }

    public static int[] calcularTempoFoguete(int tempo_foguete_b){
        int[] dados_foguete_B = new int[3];
        
        int segundos_para_minutos = arredondarValores(tempo_foguete_b / 60);
        int minutos_para_horas = arredondarValores(segundos_para_minutos /60);

        int segundos = tempo_foguete_b;
        dados_foguete_B[0] = segundos;

        int minutos = segundos_para_minutos;
        dados_foguete_B[1] = minutos;

        int horas = minutos_para_horas;
        dados_foguete_B[2] = horas;
        return dados_foguete_B;

    }

    public static void main(String[] args) {
        int tempo_foguete_a = 259200;
        int tempo_foguete_b = tempo_foguete_a / 2;
        int[] tempoFogueteB = calcularTempoFoguete(tempo_foguete_b);
        exibirVetor(tempoFogueteB);




    }
}
