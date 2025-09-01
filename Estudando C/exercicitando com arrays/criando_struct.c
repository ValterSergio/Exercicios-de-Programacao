# include <stdio.h>

struct livro
{
    char titulo[60];
    char autor[60];
    double preco;
} livro1;

int main(void)
{

    struct livro livro1 = {"Aprendendo struct", "Em C", 965.54};

    printf("Titulo: %s\n", livro1.titulo);
    printf("Autor: %s\n", livro1.autor);
    printf("Preco: %.2f\n", livro1.preco);

}