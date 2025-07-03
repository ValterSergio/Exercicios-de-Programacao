# include <stdio.h>

int main(){
    float altura;
    float largura;

    // entrada
    printf("Informe a altura da parede: ");
    scanf("%f", &altura);

    printf("Informe a largura da parede: ");
    scanf("%f", &largura);

    // processamento

    // validar altura e largura
    if (altura > 0 && largura > 0){
        float area = altura * largura;
        float tinta = area / 2; // 1 litro cobre 2m²

        // saida
        printf("Para uma parede como a informada:\n");
        printf("Altura: %.2f\n", altura);
        printf("Largura: %.2f\n", largura);
        printf("Area Total: %.2f\n", area);
        printf("Total de tinta em Litros: %.2f\n", tinta);
        
    } else {
        printf("Erro: Informe Valores acima de 0 para altura e largura.\n");
    }
    return 0;
}