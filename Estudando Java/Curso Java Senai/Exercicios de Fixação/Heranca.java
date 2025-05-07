class Pessoa {
    private String nome;
    private int idade;

    public Pessoa(String nome, int idade) {
        this.nome = nome;
        this.idade = idade;
    }

    public void apresentar() {
        System.out.println("Me chamo " + getNome());
        System.out.println("Tenho " + getIdade() + " anos de idade");
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public int getIdade() {
        return idade;
    }

    public void setIdade(int idade) {
        this.idade = idade;
    }
}

class Aluno extends Pessoa {
    private String curso;

    public Aluno(String nome, int idade) {
        super(nome, idade);
    }

    public void estudar() {
        System.out.println(getNome() + " está estudando.");
    }

    public String getCurso() {
        return curso;
    }

    public void setCurso(String curso) {
        this.curso = curso;
    }
}

class Professor extends Pessoa {
    private String disciplina;

    public Professor(String nome, int idade) {
        super(nome, idade);
    }

    public void ensinar() {
        System.out.println("Professor " + getNome() + " está ensinando.");
    }

    public String getDisciplina() {
        return disciplina;
    }

    public void setDisciplina(String disciplina) {
        this.disciplina = disciplina;
    }
}

public class Heranca {
    public static void main(String[] args) {
        Aluno aluno1 = new Aluno("Aluno1", 21);
        Professor prof1 = new Professor("Prof1", 26);

        aluno1.apresentar();
        prof1.apresentar();

        aluno1.estudar();
        prof1.ensinar();
    }
}

