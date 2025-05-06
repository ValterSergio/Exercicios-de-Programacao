/*
 * Agregação: Aluno existe independente de curso
 * Aluno: Agrega o Curso, mas o curso vai continuar lá mesmo sem alunos
 * Curso: Pode ter Varios Alunos
 * ControledeAlunos: classe Principal para gerenciar a gregação
 */

public class ControleDeAlunos {
    public static void main(String[] args) {
        // criar 3 alunos
        Aluno valter = new Aluno("Valter", 31);
        Aluno wagner = new Aluno("Wagner", 33);
        Aluno wictor = new Aluno("Wictor", 26);

        // criar curso de qualquerCoisa
        Curso qualquerCoisa = new Curso("Qualquer Coisa", 240);

        // adicionar os alunos no curso
        qualquerCoisa.adicionarAluno(wictor);
        qualquerCoisa.adicionarAluno(wagner);
        qualquerCoisa.adicionarAluno(valter);
        
        // exibir alunos
        qualquerCoisa.exibirAlunosMatriculados();
    }
    
}

class Aluno {
    String nome;
    int idade;

    public Aluno(String nome, int idade){
        this.nome = nome;
        this.idade = idade;

    }

    public void exibir_aluno(){
        System.out.printf("\nAluno: %s    | Idade: %d", this.nome, this.idade);
    }
}

class Curso {
    String nomeCurso;
    int cargaHoraria;
    int limitePorTurma = 10;
    Aluno[] turmaAlunos;

    public Curso(String nomeCurso, int cargaHoraria){
        this.nomeCurso = nomeCurso;
        this.cargaHoraria = cargaHoraria;
        this.turmaAlunos = new Aluno[this.limitePorTurma];
    }

    public void adicionarAluno(Aluno aluno){
        boolean guardado = false;
        for (int i = 0; i < turmaAlunos.length; i++) {
            if (this.turmaAlunos[i] == null){
                this.turmaAlunos[i] = aluno;
                guardado = true;
                break;
            }
        }

        if (guardado) {
            System.out.printf("\nAluno %s Matriculado com Sucesso no curso de %s", aluno.nome, this.nomeCurso);
        } else {
            System.out.println("\nA Sala está cheia, não é possivel realizar matricula !!!");
        }
    }

    public void exibirAlunosMatriculados(){
        for (int i = 0; i < turmaAlunos.length; i++) {
            if (turmaAlunos[i] != null){
                turmaAlunos[i].exibir_aluno();
            }
        }
    }

}
