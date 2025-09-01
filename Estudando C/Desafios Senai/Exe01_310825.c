#include <stdio.h>
#include <stdlib.h>

double ObterSalarioBase();
int ObterTempoServico();
int ObterNotaDesempenho();
int CalcularBonus(int tempo, int nota);
double CalcularSalarioFinal(int bonus, double salario);

int main(){
    // VAR
    double salarioBase;
    double salarioFinal;
    int tempoServico;
    int notaDesempenho;
    int bonusRecebido;

    // Entrada
    salarioBase = ObterSalarioBase();
    tempoServico = ObterTempoServico();
    notaDesempenho = ObterNotaDesempenho();

    // processamento
    bonusRecebido = CalcularBonus(tempoServico, notaDesempenho);
    salarioFinal = CalcularSalarioFinal(bonusRecebido, salarioBase);

    // saida
    printf("\nSalario Base: %.2f", salarioBase);
    printf("\nBonus Recebido: %i%%", bonusRecebido);
    printf("\nSalario Final: %.2f", salarioFinal);
}

double CalcularSalarioFinal(int bonus, double salario){
    return salario + (salario * ((double) bonus / 100)); 
}

int CalcularBonus(int tempo, int nota){
    int bonus;
    // calcular bonus por tempo
    if (tempo < 3){
        printf("\nTempo de servico Insuficiente para bonus\n");
        bonus = 0;
    } else if (tempo >= 3 && tempo <= 5){
        printf("\nBonus por tempo de servico: 5%%\n");
        bonus = 5;
    } else {
        printf("\nBonus por tempo de servico: 10%%\n");
        bonus = 10;
    }
    // calcular bonus por desempenho
    if (nota < 4){
        printf("\nDesempenho muito Baixo: Bonus anulado\n");
        bonus = 0;
    } else if (nota >= 4 && nota <= 7){
        printf("\nDesempenho mediano: Bonus inalterado: %i%%\n", bonus);
    } else {
        bonus = bonus * 2;
        printf("\nDesempenho Excelente: Bonus dobrado: %i%%\n", bonus);
    }
    return bonus;

}

int ObterNotaDesempenho(){
    int nota;
    printf("Informe a nota de desempenho: ");
    scanf("%i", &nota);
    if (nota >= 0 && nota <=10){
        return nota;
    } else {
        printf("\nInforme Apenas valores no intervalo de 0-10 !!!\n");
        exit(-1);
    }
}

int ObterTempoServico(){
    int tempo;
    printf("Informe o tempo de servico: ");
    scanf("%i", &tempo);
    if (tempo > 0){
        return tempo;
    } else {
        printf("Informe Apenas valores Positivos!!!");
        exit(-1);
    }    
}

double ObterSalarioBase(){
    double salario;
    printf("Informe o salario base: ");
    scanf("%lf", &salario);
    if (salario > 0){
        return salario;
    } else {
        printf("\nInforme Apenas Valores Positivos !!!");
        exit(-1);
    }
}
