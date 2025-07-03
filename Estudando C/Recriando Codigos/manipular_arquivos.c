# include <stdio.h>

int main(){
    FILE *arquivo = fopen("meu_arquivo.txt", "w");
    
    // verificar se abriu corretamente
    if (arquivo == NULL){
        perror("Erro ao abrir o arquivo.");
        return 1;
    }

    // frase para escrita
    char texto[] = "Ola mundo !!!";

    // escrever em uma linha
    fputs(texto, arquivo);

    // forçar a gravação no disco, já que as vezes ele pode ficar no buffer
    fflush(arquivo);

    // fechar o arquivo
    fclose(arquivo);

    return 0;
}