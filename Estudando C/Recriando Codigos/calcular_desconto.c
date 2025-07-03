# include <stdio.h>

int main(){
    float valor;
    float desconto;
    
    // entrada
    printf("Informe o valor do produto: ");
    scanf("%f", &valor);

    printf("Informe o valor do desconto: ");
    scanf("%f", &desconto);

    // processamento

    // - validar entradas
    if (valor > 0 && desconto > 0 && desconto < 100){
    float valor_final = valor - (valor * (desconto / 100));

    // saida
    printf("O produto com o valor de %.2f reais teve um desconto de %.2f porcento e agora passa a custar %.2f reais.", valor, desconto, valor_final);
    } else {
        printf("Valor de produto deve ser maior que 0.\nValor de desconto deve ser maior que 0 e menor que 100.");
    }
    return 0;
}