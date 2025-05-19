class ContaBancaria {
    private String titular;
    private double saldo;

    public ContaBancaria(String titular){
        this.titular = titular;
        this.saldo = 0;
    }

    public String getTitular(){
        return titular;
    }

    public double getSaldo(){
        return saldo;
    }

    public boolean setSaldo(double novoSaldo){
        if (novoSaldo < 0){
            System.out.println("Conta não pode ficar no vermelho");
            return false;
        } else {
            System.out.println("Saldo alterado com sucesso");
            this.saldo = novoSaldo;
            return true;
        }
    }

    public boolean depositar(double valor){
        if (valor <= 0){
            System.out.println("Não é possível realizar depósitos negativos");
            return false;
        } else {
            double calcular = getSaldo() + valor;
            return setSaldo(calcular);
        }
    }

    public boolean sacar(double valor){
        boolean valor_positivo = valor >= 0;
        boolean saldo_suficiente = getSaldo() >= valor;

        if (saldo_suficiente && valor_positivo) {
            double calcular = getSaldo() - valor;
            return setSaldo(calcular);
        }

        System.out.println("Saque não realizado: valor inválido ou saldo insuficiente");
        return false;
    }
}

class ContaPoupanca extends ContaBancaria {
    private double taxaJuros;

    public ContaPoupanca(String titular, double taxaJuros){
        super(titular);
        this.taxaJuros = taxaJuros;
    }

    public void aplicarJuros(){
        double calcular = getSaldo() + (getSaldo() * taxaJuros);
        setSaldo(calcular);
    }
}

public class exercicio_4 {
    public static void main(String[] args) {
        String nome = "Poupança 1";
        double taxaJuros = 0.1; // 10%

        ContaPoupanca poupanca = new ContaPoupanca(nome, taxaJuros);
        System.out.println("Saldo atual: " + poupanca.getSaldo());

        poupanca.depositar(100);
        System.out.println("Saldo após depósito: " + poupanca.getSaldo());

        poupanca.aplicarJuros();
        System.out.println("Saldo após aplicação de juros: " + poupanca.getSaldo());
    }
}
