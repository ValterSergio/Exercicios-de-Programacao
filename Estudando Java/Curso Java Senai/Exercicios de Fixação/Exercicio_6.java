// Classe base Funcionario
class Funcionario {
    protected String nome;
    protected double salarioBase;

    public Funcionario(String nome, double salarioBase) {
        this.nome = nome;
        this.salarioBase = salarioBase;
    }

    public double calcularSalario() {
        return salarioBase;
    }

    public String getNome() {
        return nome;
    }
}

// Classe Gerente herda de Funcionario
class Gerente extends Funcionario {
    protected double bonus;

    public Gerente(String nome, double salarioBase, double bonus) {
        super(nome, salarioBase);
        this.bonus = bonus;
    }

    @Override
    public double calcularSalario() {
        return salarioBase + bonus;
    }
}

// Classe Diretor herda de Gerente
class Diretor extends Gerente {
    private double participacaoLucros;

    public Diretor(String nome, double salarioBase, double bonus, double participacaoLucros) {
        super(nome, salarioBase, bonus);
        this.participacaoLucros = participacaoLucros;
    }

    @Override
    public double calcularSalario() {
        return salarioBase + bonus + participacaoLucros;
    }
}

// Classe principal
public class Exercicio_6 {
    public static void main(String[] args) {
        // Criando os funcionários com base no enunciado

        Funcionario f1 = new Funcionario("Funcionário Comum", 3000);
        Gerente g1 = new Gerente("Gerente 1", 3000, 0);
        Gerente g2 = new Gerente("Gerente 2", 5000, 1000);
        Diretor d1 = new Diretor("Diretor 1", 1000, 0, 0);
        Diretor d2 = new Diretor("Diretor 2", 8000, 2000, 5000); // 2000 + 3000 = 5000 de PL

        // Exibindo os salários
        System.out.println(f1.getNome() + " - Salário: R$" + f1.calcularSalario());
        System.out.println(g1.getNome() + " - Salário: R$" + g1.calcularSalario());
        System.out.println(g2.getNome() + " - Salário: R$" + g2.calcularSalario());
        System.out.println(d1.getNome() + " - Salário: R$" + d1.calcularSalario());
        System.out.println(d2.getNome() + " - Salário: R$" + d2.calcularSalario());
    }
}
