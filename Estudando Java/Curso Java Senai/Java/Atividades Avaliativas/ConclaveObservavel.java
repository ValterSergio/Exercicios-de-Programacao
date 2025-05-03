// aula 30/04
public class ConclaveObservavel {
    // Atributos privados
    private int numeroCardeaisPresentes = 0;
    private boolean fumacaVisivel = false;
    private String corFumaca = null;

    // obtem o número de cardeais presentes
    public int obterNumeroCardeaisPresentes() {
        return numeroCardeaisPresentes;
    }

    // informa se a fumaça esta visível
    public boolean isFumacaVisivel() {
        return fumacaVisivel;
    }

    // obtem a cor da fumaça visível
    public String obterCorFumaca() {
        return corFumaca;
    }

    // Atualiza numero cardeais (pode adicionar ou remover)
    public void atualizarPresencaCardeal(int variacao) {
        numeroCardeaisPresentes += variacao;
        if (numeroCardeaisPresentes < 0) {
            numeroCardeaisPresentes = 0;
        }
    }

    // Atualiza a fumaça visível e sua cor
    public void sinalizarFumaca(String cor) {
        if (cor != null && (cor.equalsIgnoreCase("branca") || cor.equalsIgnoreCase("preta"))) {
            fumacaVisivel = true;
            corFumaca = cor;
        } else {
            fumacaVisivel = false;
            corFumaca = null;
        }
    }

    // Método principal sem usar construtor
    public static void main(String[] args) {

        ConclaveObservavel conclave = new ConclaveObservavel();

        // Exibindo o estado inicial
        System.out.println("Número de Cardeais Presentes: " + conclave.obterNumeroCardeaisPresentes());
        System.out.println("Fumaça Visível: " + conclave.isFumacaVisivel());
        System.out.println("Cor da Fumaça: " + conclave.obterCorFumaca());

        System.out.println("----------------------------------");

        // Simulando chegada de cardeais
        conclave.atualizarPresencaCardeal(115);
        System.out.println("Após chegada de cardeais:");
        System.out.println("Número de Cardeais Presentes: " + conclave.obterNumeroCardeaisPresentes());

        System.out.println("----------------------------------");

        // Simulando fumaça preta
        conclave.sinalizarFumaca("preta");
        System.out.println("Após sinalizar fumaça preta:");
        System.out.println("Fumaça Visível: " + conclave.isFumacaVisivel());
        System.out.println("Cor da Fumaça: " + conclave.obterCorFumaca());

        System.out.println("----------------------------------");

        // Simulando saída de cardeal
        conclave.atualizarPresencaCardeal(-1);
        System.out.println("Após saída de um cardeal:");
        System.out.println("Número de Cardeais Presentes: " + conclave.obterNumeroCardeaisPresentes());

        System.out.println("----------------------------------");

        // Simulando fumaça branca
        conclave.sinalizarFumaca("branca");
        System.out.println("Após sinalizar fumaça branca:");
        System.out.println("Fumaça Visível: " + conclave.isFumacaVisivel());
        System.out.println("Cor da Fumaça: " + conclave.obterCorFumaca());

        System.out.println("----------------------------------");

        // Tentando sinalizar fumaça inválida
        conclave.sinalizarFumaca("azul");
        System.out.println("Após tentativa de fumaça inválida:");
        System.out.println("Fumaça Visível: " + conclave.isFumacaVisivel());
        System.out.println("Cor da Fumaça: " + conclave.obterCorFumaca());
    }
}
