import java.util.Scanner;

public class Exercicio05_SalarioMensal {

    public static void main(String[] args) {
        // Cria o Scanner para ler do teclado
        Scanner scanner = new Scanner(System.in);

        // Solicita a quantidade de horas trabalhadas
        System.out.print("Informe o número de horas trabalhadas no mês: ");
        double horasTrabalhadas = scanner.nextDouble();

        // Solicita o valor recebido por hora
        System.out.print("Informe o valor da sua hora de trabalho: R$ ");
        double valorHora = scanner.nextDouble();

        // Calcula o salário bruto (sem descontos)
        double salario = horasTrabalhadas * valorHora;

        // Exibe o salário final
        System.out.println("Seu salário neste mês será: R$ " + salario);

        // Fecha o scanner
        scanner.close();
    }
}
