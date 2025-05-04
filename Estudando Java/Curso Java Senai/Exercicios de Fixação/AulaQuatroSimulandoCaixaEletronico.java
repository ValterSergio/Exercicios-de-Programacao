
import java.util.Scanner;

public class AulaQuatroSimulandoCaixaEletronico  {
    private static Scanner input = new Scanner(System.in);
    
    public static void main(String[] args) {
        // Criar Cliente Fictício
        String nomeClienteSalvo, obterCliente, senhaClienteSalva, obterSenha;
        boolean acessoLiberado;

        acessoLiberado = false;
        nomeClienteSalvo = "valter";
        senhaClienteSalva = "valter";
        int tentativas = 3;

        // Processo de Login
        while (tentativas > 0) {
            System.out.println("Tentativas restantes: " + tentativas);
            System.out.println("Bem-vindo, informe seu nome:");
            obterCliente = input.nextLine();

            if (obterCliente.equals(nomeClienteSalvo)) {
                // Nome correto, agora pedir a senha
                while (tentativas > 0) {
                    System.out.println("Tentativas restantes: " + tentativas);
                    System.out.println("Informe a senha:");
                    obterSenha = input.nextLine();

                    if (obterSenha.equals(senhaClienteSalva)) {
                        System.out.println("Acesso Liberado");
                        acessoLiberado = true;
                        tentativas = 0; // Finaliza tentativas
                    } else {
                        System.out.println("Senha incorreta");
                        tentativas = tentativas - 1;
                    }
                }
            } else {
                System.out.println("Nome não identificado");
                tentativas = tentativas - 1;
            }
        }

        // Verificar se o acesso foi liberado
        if (!acessoLiberado) {
            System.out.println("Acesso Negado");
            System.exit(0);
        }

        // Início da lógica de Conta Bancária
        double saldoInicial, saldoAtual, valorDeposito, valorSaque;

        System.out.println("Informe o saldo inicial:");
        saldoInicial = input.nextDouble();
        saldoAtual = saldoInicial;

        int escolher = 1;
        // Menu de operações bancárias
        while (escolher > 0) {
            System.out.println("1 - Sacar");
            System.out.println("2 - Depositar");
            System.out.println("3 - Ver Saldo");
            System.out.println("0 - Sair");
            System.out.println("Escolha uma opção (0, 1, 2, 3):");
            escolher = input.nextInt();

            if (escolher == 1) {
                // Opção de Saque
                System.out.println("Informe o valor do Saque:");
                valorSaque = input.nextDouble();

                if (valorSaque > 0) {
                    if (valorSaque <= saldoAtual) {
                        saldoAtual = saldoAtual - valorSaque;
                        System.out.println("Sacando Dinheiro");
                    } else {
                        System.out.println("Valor de saque deve ser menor ou igual ao saldo atual");
                    }
                } else {
                    System.out.println("Valor de saque deve ser maior que zero");
                }
            }

            if (escolher == 2) {
                // Opção de Depósito
                System.out.println("Informe o valor para depósito:");
                valorDeposito = input.nextDouble();

                if (valorDeposito > 0) {
                    saldoAtual = saldoAtual + valorDeposito;
                    System.out.println("Depositando Dinheiro");
                } else {
                    System.out.println("Valor de depósito deve ser maior que zero");
                }
            }

            if (escolher == 3) {
                // Visualizar saldo
                System.out.println("Visualizando Saldo Atual: " + saldoAtual);
            }
        }

        System.out.println("Saindo do programa");
    }
}

