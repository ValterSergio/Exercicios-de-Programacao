import java.util.Scanner;

class Cliente{
    private String nome;
    private String tipoConta;
    private int valorMinimoDeposito;
    private int idade;
    private Double saldo;
    
    public Cliente(String nome, int idade, String tipoConta){
        this.nome = nome;
        this.idade = idade;
        this.tipoConta = tipoConta;
        this.saldo = 0.0;
        this.valorMinimoDeposito = 50;

    }

    public String getNome(){
        return this.nome;
    }

    public String getTipoConta(){
        return this.tipoConta;
    }
    
    public double getSaldo(){
        return this.saldo;
    }

    public int getIdade(){
        return this.idade;
    }

    public void setNome(String novoNome){
        this.nome = novoNome;
    }

    public void setIdade(int idade){
        this.idade = idade;
    }

    public void setTipoConta(String tipoConta){
        this.tipoConta = tipoConta;
    }

    public void setSaldo(double saldo){
        if (saldo > this.valorMinimoDeposito) {
            this.saldo = saldo; 
        }
    }

    public void depositar(double valor){
        if (this.valorMinimoDeposito >= valor) {
            System.out.println("Valor Minimo para deposito: " + this.valorMinimoDeposito);
        }

        System.out.println("Depósito Realizado com Sucesso");
        double calcular = getSaldo() + valor;
        setSaldo(calcular); // atualiza o estado saldo da classe
        }
    
    public void exibirCliente(){
        System.out.println("Tipo de Conta: " + getTipoConta());
        System.out.println("Nome: " + getNome());
        System.out.println("Idade: " + getIdade());
        System.out.println("Saldo Atual: " + getSaldo());
    }
}

public class AulaDiaSeteDeMaioContaBancaria{


    public static String tipoContaUsuario(Scanner scanner){
        boolean flag = true;
        String tipoConta = "Conta Corrente ( padrão )";
        while (flag) {
            System.out.println("Informe um tipo de conta: ");
            System.out.println("1 - Conta Corrente ");
            System.out.println("2 - Conta Poupança ");
            System.out.println("0 - Cancelar e Sair");
            System.out.print("Escolha uma opção: ");
            int escolha = scanner.nextInt();
            scanner.nextLine(); // limpar scanner
            switch (escolha) {
                case 1:
                    tipoConta = "Conta Corrente";
                    flag = false; // que◘bra o loop
                    break;
                
                case 2:
                    tipoConta = "Conta Poupança";
                    flag = false; // quebra o loop
                    break;
                
                case 0:
                    flag = false; // quebra o loop
                    break;

                default:
                    System.out.println("Erro: informe um número válido (0, 1 ou 2)");
                    break;
            }
        
        }
        return tipoConta;

    }


    public static String obterEntradaString(Scanner scanner, String infoEntrada){
        System.out.print("Digite " + infoEntrada + ": ");
        return scanner.nextLine();
    }

    public static double obterEntradaNumerica(Scanner scanner, String infoEntrada){
        System.out.print("Informe " + infoEntrada + ": ");
        return scanner.nextDouble();
    }

    public static void main(String[] args) {
        
        //  entradas
        Scanner scanner = new Scanner(System.in);
        String nome = obterEntradaString(scanner, "Nome");
        int idade = ( int ) obterEntradaNumerica(scanner, "Idade");
        scanner.nextLine(); // limpar scanner
        String tipoConta = tipoContaUsuario(scanner);

        // Criar cliente
        Cliente cliente1 = new Cliente(nome, idade, tipoConta);

        // processamento e saida do programa
        boolean flag = true;
        while (flag) {
            System.out.println();
            System.out.println("Seja Bem vindo " + cliente1.getNome());
            System.out.println("Saldo Atual: " + cliente1.getSaldo());
            System.out.println("1 - Realizar deposito");
            System.out.println("2 - Exibir Detalhes");
            System.out.println("3 - Sair");
            int escolha = (int) obterEntradaNumerica(scanner, "uma Opção");
            System.out.println();
            switch (escolha) {
                case 1:
                    double valor = obterEntradaNumerica(scanner, "valor Depósito");
                    double calcularSaldo = cliente1.getSaldo() + valor;
                    cliente1.setSaldo(calcularSaldo);
                    break;
                
                case 2:
                    cliente1.exibirCliente();
                    break;
                case 3:
                    System.out.println("Saindo...");
                    flag = false;
                default:
                    System.out.println("Erro: Entrada invalida, digite numeros de 1 a 3 !!");
                    break;
            }
        
        System.out.println("Volte sempre " + cliente1.getNome());
        

            
            
        
        
        
    }
}
}