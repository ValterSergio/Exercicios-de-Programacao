public class exercicio_10 {
    
    public class ProcessamentoPagamentos {

        // Classe CartaoCredito
        static class CartaoCredito {
            private String numero;
    
            public CartaoCredito(String numero) {
                this.numero = numero;
            }
    
            // Método para processar pagamento e exibir os 4 últimos dígitos
            public void processarPagamento(double valor) {
                if (numero.length() >= 4) {
                    String ultimosDigitos = numero.substring(numero.length() - 4);
                    System.out.println("Pagamento de R$" + valor + " processado com o Cartão de Crédito.");
                    System.out.println("Últimos 4 dígitos do cartão: " + ultimosDigitos);
                } else {
                    System.out.println("Número de cartão inválido.");
                }
            }
        }
    
        // Classe Pix
        static class Pix {
            private String chave;
    
            public Pix(String chave) {
                this.chave = chave;
            }
    
            // Método para processar pagamento e exibir a chave Pix
            public void processarPagamento(double valor) {
                System.out.println("Pagamento de R$" + valor + " processado via Pix.");
                System.out.println("Chave Pix: " + chave);
            }
        }
    
        // Método main
        public static void main(String[] args) {
            // Criando instâncias
            CartaoCredito cartao = new CartaoCredito("1234567812345678");
            Pix pix = new Pix("chave@pix.com");
    
            // Processando pagamentos
            cartao.processarPagamento(150.75); // Cartão de Crédito
            System.out.println(); // Linha em branco para separar
            pix.processarPagamento(200.50);  // Pix
        }
    }
}