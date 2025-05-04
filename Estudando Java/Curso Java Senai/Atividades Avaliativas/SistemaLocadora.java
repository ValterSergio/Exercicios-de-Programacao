import java.util.Scanner;

class Veiculo {
    private String modelo;
    private String placa;
    private int ano;
    private boolean disponivel;

    public Veiculo(String modelo, String placa, int ano) {
        this.modelo = modelo;
        this.placa = placa;
        this.ano = ano;
        this.disponivel = true; // Inicia como disponível
    }

    public String getModelo() {
        return modelo;
    }

    public String getPlaca() {
        return placa;
    }

    public int getAno() {
        return ano;
    }

    public boolean isDisponivel() {
        return disponivel;
    }

    public void setDisponivel(boolean disponivel) {
        this.disponivel = disponivel;
    }

    public String getStatus() {
        return disponivel ? "Disponível" : "Locado";
    }
}

public class SistemaLocadora {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Veiculo[] frota = new Veiculo[5];
        int quantidadeVeiculos = 0;
        int opcao;

        do {
            System.out.println("\n--- Sistema de Locadora de Veículos ---");
            System.out.println("1 - Cadastrar Veículo");
            System.out.println("2 - Listar Veículos");
            System.out.println("3 - Locar Veículo");
            System.out.println("4 - Devolver Veículo");
            System.out.println("5 - Relatório Geral");
            System.out.println("0 - Encerrar");
            System.out.print("Escolha uma opção: ");
            opcao = scanner.nextInt();
            scanner.nextLine(); // Limpar buffer

            switch (opcao) {
                case 1:
                    if (quantidadeVeiculos < 5) {
                        System.out.print("Modelo: ");
                        String modelo = scanner.nextLine();
                        System.out.print("Placa: ");
                        String placa = scanner.nextLine();
                        System.out.print("Ano: ");
                        int ano = scanner.nextInt();
                        scanner.nextLine(); // Limpar buffer

                        frota[quantidadeVeiculos] = new Veiculo(modelo, placa, ano);
                        quantidadeVeiculos++;
                        System.out.println("Veículo cadastrado com sucesso!");
                    } else {
                        System.out.println("Frota cheia! Não é possível cadastrar mais veículos.");
                    }
                    break;

                case 2:
                    System.out.println("\n--- Lista de Veículos ---");
                    for (int i = 0; i < quantidadeVeiculos; i++) {
                        System.out.println(i + " - " + frota[i].getModelo() + " | " + frota[i].getPlaca() + " | " +
                                           frota[i].getAno() + " | " + frota[i].getStatus());
                    }
                    break;

                case 3:
                    System.out.print("Informe o índice do veículo para locação: ");
                    int indiceLocar = scanner.nextInt();
                    scanner.nextLine(); // Limpar buffer

                    if (indiceLocar >= 0 && indiceLocar < quantidadeVeiculos) {
                        if (frota[indiceLocar].isDisponivel()) {
                            frota[indiceLocar].setDisponivel(false);
                            System.out.println("Veículo locado com sucesso!");
                        } else {
                            System.out.println("Este veículo já está locado.");
                        }
                    } else {
                        System.out.println("Índice inválido.");
                    }
                    break;

                case 4:
                    System.out.print("Informe o índice do veículo para devolução: ");
                    int indiceDevolver = scanner.nextInt();
                    scanner.nextLine(); // Limpar buffer

                    if (indiceDevolver >= 0 && indiceDevolver < quantidadeVeiculos) {
                        if (!frota[indiceDevolver].isDisponivel()) {
                            frota[indiceDevolver].setDisponivel(true);
                            System.out.println(" Veículo devolvido com sucesso!");
                        } else {
                            System.out.println(" Este veículo já está disponível.");
                        }
                    } else {
                        System.out.println("Índice inválido.");
                    }
                    break;

                case 5:
                    int disponiveis = 0;
                    int locados = 0;
                    for (int i = 0; i < quantidadeVeiculos; i++) {
                        if (frota[i].isDisponivel()) {
                            disponiveis++;
                        } else {
                            locados++;
                        }
                    }
                    System.out.println("\n--- Relatório Geral ---");
                    System.out.println("Total de veículos: " + quantidadeVeiculos);
                    System.out.println("Disponíveis: " + disponiveis);
                    System.out.println("Locados: " + locados);
                    break;

                case 0:
                    System.out.println("Encerrando o sistema...");
                    break;

                default:
                    System.out.println("Opção inválida. Tente novamente.");
                    break;
            }
        } while (opcao != 0);

        scanner.close();
    }
}
