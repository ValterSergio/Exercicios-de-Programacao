/*
 * Ana quer saber quanto seu salário iria render no seu banco virtual.
 * Ela pretende descobrir quanto vai ter ganhado ao final de 1 ano.
 * Ana pretende poupar 15% do salário todo mês, e todo mês o banco 
 * rende 7% do valor total guardado na conta.
 * Ela quer saber o valor que ganhará apenas com os rendimentos mensais.
 */

 public class DesenvolverUmProblemaParteUm {

    /**
     * Exibe no console os valores de rendimento mês a mês.
     * @param vetor Array contendo os rendimentos mensais.
     */
    public static void exibirVetor(double[] vetor){
        for (int i = 0; i < vetor.length; i++){
            // Exibe o mês e o valor ganho com rendimento, com 2 casas decimais
            System.out.printf("Mês: %d - Valor Ganho: R$ %.2f%n", i + 1, vetor[i]);
        }
    }

    /**
     * Soma todos os rendimentos mensais para obter o total ganho no ano.
     * @param vetor Array com os rendimentos mensais.
     * @return Total acumulado de rendimentos ao final de 1 ano.
     */
    public static double somarGanhos(double[] vetor){
        double total = 0;
        for (int i = 0; i < vetor.length; i++){
            // Soma os valores mês a mês
            total += vetor[i];
        }
        return total;
    }

    public static void main(String[] args) {
        int tempo_investimento = 12; // Duração do investimento: 12 meses (1 ano)
        double rendimento_porcentagem = 0.07; // Rendimento mensal do banco: 7%
        double salario = 2000; // Salário mensal de Ana
        double porcentagem_salario = 0.15; // Porcentagem do salário que será poupada: 15%
        double[] renda_mensal = new double[tempo_investimento]; // Vetor que armazena os rendimentos de cada mês

        double poupar = 0; // Acumulador do valor total guardado na conta mês a mês

        for (int i = 0; i < tempo_investimento; i++){
            
            // Calcula o rendimento do mês atual com base no valor acumulado
            double ganho = poupar * rendimento_porcentagem;

            // Armazena o rendimento arredondado no vetor mensal
            double armazenar_rendimento = Math.round(ganho);
            renda_mensal[i] = armazenar_rendimento;

            // Calcula quanto será poupado do salário no mês atual
            double guardar = salario * porcentagem_salario;

            // Adiciona o valor poupado ao total acumulado
            poupar += guardar;
        }

        // Exibe o rendimento mês a mês
        exibirVetor(renda_mensal);

        // Soma todos os rendimentos para exibir o ganho total ao final do ano
        double ganho = somarGanhos(renda_mensal);
        System.out.printf("Durante o ano o investimento vai ter rendido: R$ %.2f", ganho);
    }
}
