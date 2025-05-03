import java.util.ArrayList;
import java.util.List;

public class ClasseArrayList {
    public static void exibirLista(List clientes){
        // obtemos o numero de elementos atraves do metodo size
        for (int i = 0; i < clientes.size(); i++){
            System.out.printf("\n| Posição: %d | Cliente: %s |", i, clientes.get(i));

        }
        // pular linha
        System.out.printf("\n\n");
    }
    
    public static void main(String[] args) {
        
        // declarando e iniciando uma lista de clientes
        ArrayList<String> clientes = new ArrayList();

        // adicionando clientes
        clientes.add("Valter");
        clientes.add("Wagner");
        clientes.add("Wando");
        clientes.add("Wictor");
        clientes.add("Wanderley");

        // exibindo os clientes
        System.out.printf("Percorrendo a lista de clientes usando indice\n");
        exibirLista(clientes);
        
        System.out.printf("Removendo o cliente por posição\n");
        // Removendo o cliente por uma posição fixa
        clientes.remove(0); // remove Valter

        // exibindo a lista com o elemento removido
        exibirLista(clientes);

        // obter um cliente pela posição
        System.out.printf("Obtendo um cliente por posição: \n");
        System.out.printf("| Cliente: %s | Posição: 0 |\n", clientes.get(0));

        // verificar se existe um cliente na lista
        System.out.printf("\nBuscar um Cliente na lista pelo nome\n");
        System.out.printf("| Alvo: Wagner | Existe: %b |\n ", clientes.contains("Wagner"));

    }    
}
