/* 
Livro:  Introdução a programação em C - Os primeiros passos de um desenvolvedor
Editora: Casa do Código 
Autor: Mauricio Anichie

*/

/*
Vamos criar um jogo de adivinhação na qual o computador pensará em um número, e você jogador, precirá adivinhá-lo.

Parece simples, mas ele lhe ajudará a aprender conceitos importantes sobre programação, como:

- Ler do teclado e escrever na tela -> para interação com o usúario
- Armazenar valores na memória e manipulá-los
- Executar operações matemáticas em cima dessas variáveis
- Entender os diferentes tipos de variáveis
- Tomar decisões no programa
- Usar laços de repetição
*/

# include <stdio.h> // standard I/O -> Entrada e saída de padrão

// Função main - ela que é executada quando roda o arquivo .exe, .out e etc.
int main(){

    printf("-------------------------------------------------------");
    printf("\n\t-- Bem-vindo ao Jogo da Adivinhacao --\n");
    printf("-------------------------------------------------------");

    /*
        O arquivo deve ser "Compilado", estou usando o GCC
        
        - sintaxe: gcc nomeArquivo.c -o nomeArquivo
        - Cada mudança no arquivo ele deve ser compilado novamente
    */

    // variaveis repetidas podem ocasionar error: redefinition of "namevariavel" -> redefinição de variavel
    int numerosecreto = 42;

    // precisamos usar mascaras para exibir variaveis
    printf("\nO numero secreto e %d", numerosecreto);
   
    /*
     - Scanf -> scanf(tipo de dado, variavel para guardar a entrada)
     - O tipo de dado deve ser passado como mascara "%d"
    */

    int chute;
    printf("\nChute um numero: ");
    scanf("%d", &chute);
    printf("Seu chute foi: %d", chute);

    



}


