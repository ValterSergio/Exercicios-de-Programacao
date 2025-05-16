public class AulaDiaSeisDeMaioCadastroAlunos {

    
    public static void main(String[] args) {
        Aluno aluno1 = new Aluno("Aluno1", 123);
        Aluno aluno2 = new Aluno("Aluno2", 123);
        Aluno aluno3 = new Aluno("Aluno3", 123);
        
        Aluno[] lista = new Aluno[3];
        lista[0] = aluno1;
        lista[1] = aluno2;
        lista[2] = aluno3;

        for (int i = 0; i < lista.length; i++) {
            lista[i].adicionarNota(6);
            lista[i].adicionarNota(6);
            lista[i].adicionarNota(6);
            lista[i].exibirNotas();
        }
    }
}

class Aluno {
    private String nome;
    private int matricula;
    private int totalBimestres = 3;
    private double[] notasRegistradas;
    private double media;

    public Aluno(String nome, int matricula) {
        this.nome = nome;
        this.matricula = matricula;
        this.notasRegistradas = new double[totalBimestres];
        this.media = 0;
    }

    public void setTotalBimestres(int total){
        this.totalBimestres = total;
    }

    public double getMedia(){
        return this.media;
    }

    public void setMedia(double valor){
        this.media = valor;
    }

    public String getNome() {
        return this.nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public int getMatricula() {
        return this.matricula;
    }

    public void setMatricula(int matricula) {
        this.matricula = matricula;
    }

    public void adicionarNota(double nota) {
        for (int i = 0; i < notasRegistradas.length; i++) {
            if (notasRegistradas[i] == 0.0) {
                notasRegistradas[i] = nota;
                break;
            }
        }
    }

    public void exibirNotas() {
        calcularMedia();
        System.out.println("------------------------------------------------------");
        System.out.println("Dados do Aluno:");
        System.out.println("------------------------------------------------------");
        System.out.printf("Aluno: %s \nMatricula: %d\n", this.nome, this.matricula);
        System.out.println("------------------------------------------------------☻");
        System.out.println("\t--- Notas registradas ---");
        for (int i = 0; i < notasRegistradas.length; i++) {
            System.out.printf("%dº Trimestre: %.1f%n", i + 1, notasRegistradas[i]);
        }
        System.out.println("------------------------------------------------------");
        System.out.printf("Média do Aluno: %.1f%n", this.media);
        System.out.println("------------------------------------------------------");
    }

    public void calcularMedia() {
        double soma = 0;
        for (double nota : notasRegistradas) {
            soma += nota;
        }
        setMedia((soma / notasRegistradas.length));
    }

}

