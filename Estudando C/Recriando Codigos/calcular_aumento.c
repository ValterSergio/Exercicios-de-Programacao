# include <stdio.h>

float calcular_aumento(float valor, float percentual){
    return valor + (valor * (percentual / 100));
}

float obter_valor(){
    float salario;
    printf("Digite o salario atual: ");
    scanf("%f", &salario);
    if (salario > 0){
        return salario;
    } else {
        printf("Erro: Salario deve ser maior que zero. ");
        return -1;
    }
}

float obter_percentual(){
    float percentual;
    printf("Digite o valor do aumento em %: ");
    scanf("%f", &percentual);
    if (percentual > 0 && percentual < 100){
        return percentual;
    } else {
        printf("Erro: Informe um valor de percentual entre maior que 0 e menor que 100");
        return -1;
    }
}

int main(){
    while (1)
    {
        float salario = obter_valor();
        float desconto = obter_percentual();
        if (salario > 0 && desconto > 0){
            // calcular aumento
            float novo_salario = calcular_aumento(salario, desconto);
            printf("Salario Anterior: %.2f", salario);
            printf("\nNovo Sálario: %.2f", novo_salario);
            return 0;
        } else {
            printf("Tente Novamente.");
        }
    }
    
}