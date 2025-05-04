import java.util.Scanner;
import java.util.Locale;

// Classe que representa um produto
class Produto {
    private String nome;
    private int total_estoque;
    private float preco_unitario;

    // Construtor para criar produto
    public Produto(String nome, int total_estoque, float preco_unitario) {
        this.nome = nome;
        this.total_estoque = total_estoque;
        this.preco_unitario = preco_unitario;
    }

    // Métodos de acesso (getters)
    public String getNome() {
        return nome;
    }

    public int getTotalEstoque() {
        return total_estoque;
    }

    public float getPrecoUnitario() {
        return preco_unitario;
    }

    // Métodos para alterar valores (setters)
    public void setNome(String novo_nome) {
        nome = novo_nome;
    }

    public void setTotalEstoque(int novo_estoque) {
        total_estoque = novo_estoque;
    }

    public void setPrecoUnitario(float novo_preco) {
        preco_unitario = novo_preco;
    }

    // Exibe as informações do produto
    public void exibirProduto() {
        System.out.println("Produto: " + getNome());
        System.out.println("Total em Estoque: " + getTotalEstoque());
        System.out.println("Preço Unitário: " + getPrecoUnitario());
    }
}

// Classe para controlar os produtos no estoque
class ControleDeEstoque {
    private int limite = 5;
    private Produto[] produtosGuardados;

    // Busca um produto pelo nome
    public Produto buscaProduto(String nome){
        for (int i = 0; i < produtosGuardados.length; i++) {
            if (produtosGuardados[i] != null) {
                String nomeProduto = produtosGuardados[i].getNome();
                if (nomeProduto.equals(nome)){
                    return produtosGuardados[i];
                }
            }
        }
        return null;
    }

    // Construtor do estoque com limite de produtos
    public ControleDeEstoque(int limite) {
        this.produtosGuardados = new Produto[limite];
        this.limite = limite;
    }

    public int getLimite(){
        return this.limite;
    }

    public Produto[] getVetor(){
        return this.produtosGuardados;
    }

    // Exibe todos os produtos cadastrados
    public void exibirEstoque() {
        for (Produto produto : produtosGuardados) {
            if (produto != null) {
                produto.exibirProduto();
            } else {
                break;
            }
        }
    }

    // Atualiza o vetor de produtos
    private void atualizarEstoque(Produto[] novoEstoque) {
        this.produtosGuardados = novoEstoque;
    }

    // Checa se há espaço livre no vetor
    public boolean checarTamanhoVetor(){
        Produto[] vetor = this.getVetor();
        int espaco_livre = 0;
        for (int i = 0; i < vetor.length; i++){
            if (vetor[i] == null){
                espaco_livre++;
            }
        }
        return espaco_livre > 0;
    }
    // conta o total de espaço livre no vetor
    public int espacoLivre(){
        Produto[] vetor = this.getVetor();
        int espaco_livre = 0;
        for (int i = 0; i < vetor.length; i++){
            if (vetor[i] == null){
                espaco_livre++;
            }
        }
        return espaco_livre;
    }
    
    
    // Adiciona um produto novo no estoque
    public boolean adicionarProduto(Produto novo_produto) {
        for (int i = 0; i < produtosGuardados.length; i++) {
            if (produtosGuardados[i] == null) {
                produtosGuardados[i] = novo_produto;
                return true;
            }
        }
        return false;
    }

    // Remove um produto do estoque
    public void removerProduto(Produto produto){
        Produto[] novoVetor = new Produto[this.limite];
        int marcarPosicao = 0;
        String removerNome = produto.getNome();
        for (int i = 0; i < this.produtosGuardados.length; i++){
            if (produtosGuardados[i] != null){
                String nomeEncontrado = produtosGuardados[i].getNome();
                if (!nomeEncontrado.equals(removerNome)) {
                    novoVetor[marcarPosicao] = produtosGuardados[i];
                }
            }
            marcarPosicao++;
        }
        atualizarEstoque(novoVetor);
    }

    // Faz o cadastro de um novo produto usando Scanner
    public boolean cadastrarProduto(Scanner scanner) {
        System.out.print("Nome do Produto: ");
        String nome = scanner.nextLine();
        System.out.print("Quantidade em Estoque: ");
        int estoque = scanner.nextInt();
        System.out.print("Preço Unitário: ");
        float preco = scanner.nextFloat();
        scanner.nextLine(); // consumir quebra de linha

        Produto novoProduto = new Produto(nome, estoque, preco);
        return adicionarProduto(novoProduto);
    }
}

// Classe principal para gerenciar o sistema
public class GerenciadorDeProdutos {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in).useLocale(Locale.US);
        ControleDeEstoque estoque = new ControleDeEstoque(5);

        while (true) {
            System.out.println("---------------------------------");
            System.out.println("Gerenciamento de Produtos");
            System.out.println("---------------------------------");
            System.out.println("[1] Cadastrar Produto");
            System.out.println("[2] Listar Produtos");
            System.out.println("[3] Remover Produto");
            System.out.println("[4] Verificar Espaço Livre");
            System.out.println("[0] Sair");
            System.out.println("---------------------------------");
            System.out.print("Escolha: ");
            int opcao = scanner.nextInt();
            scanner.nextLine(); // consumir quebra de linha
            
            switch (opcao) {
                case 1:
                System.out.println("---------------------------------");
                System.out.print("Cadastrando Produto\n");
                System.out.println("---------------------------------");
                if (estoque.checarTamanhoVetor()){
                    if (estoque.cadastrarProduto(scanner)) {
                        System.out.println("Cadastro realizado.");
                    } else {
                        System.out.println("Erro no cadastro.");
                    }
                } else {
                    System.out.println("Sem espaço para novo produto.");
                }
                break;
                
                case 2:
                System.out.println("---------------------------------");
                System.out.print("Exibindo Estoque\n");
                System.out.println("---------------------------------");
                estoque.exibirEstoque();
                break;
                
                case 3:
                System.out.println("---------------------------------");
                System.out.print("Remover Produto\n");
                System.out.println("---------------------------------");
                System.out.print("Nome do Produto para Remover: ");
                String nome_produto = scanner.nextLine();
                System.out.println("---------------------------------");
                estoque.removerProduto(estoque.buscaProduto(nome_produto));
                break;
                
                case 4:
                System.out.println("---------------------------------");
                System.out.print("Verificando Armazenamento\n");
                System.out.println("---------------------------------");
                if (estoque.checarTamanhoVetor()) {
                    System.out.printf("Há %d lugares disponíveis.\n", estoque.espacoLivre());
                } else {
                    System.out.println("Estoque cheio.");
                }
                System.out.println("---------------------------------");
                break;

                case 0:
                    System.out.println("Encerrando o programa.");
                    scanner.close();
                    System.exit(0);
                    break;

                default:
                    System.out.println("Opção inválida.");
                    break;
            }  
        } 
    }
}
