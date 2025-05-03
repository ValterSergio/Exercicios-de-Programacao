import java.util.Scanner;

public class AulaDiaVinteTresDeAbrilPOO {

    private String nome;
    private int idade;

    public String getNome() {
        return this.nome;
    }

    public int getIdade() {
        return this.idade;
    }

    public void setNome(String novo) {
        if (novo != null) {
            this.nome = novo;
        } else {
            System.out.printf("Nome Vazio: %s\n", novo);
        }
    }

    public void setIdade(int novo) {
        if (novo >= 18) {
            this.idade = novo;
        } else {
            System.out.printf("Menor de Idade, não permitido: %d\n", novo);
        }
    }

    public static void main(String[] args) {
        // instanciando objetos
        AulaDiaVinteTresDeAbrilPOO valter = new AulaDiaVinteTresDeAbrilPOO();
        AulaDiaVinteTresDeAbrilPOO fulano = new AulaDiaVinteTresDeAbrilPOO();

        // Scanner
        Scanner scanner = new Scanner(System.in);

        // variáveis para receber os dados
        String obterNome;
        int obterIdade;

        // coletar dados do usuário
        System.out.print("Digite o Seu Nome: ");
        obterNome = scanner.nextLine();
        System.out.println(); // quebra de linha

        System.out.print("Digite Sua Idade: ");
        obterIdade = scanner.nextInt();
        System.out.println(); // quebra de linha

        // definir dados do primeiro objeto
        valter.setIdade(30);
        valter.setNome("Preferido Delas");

        // definir dados do segundo objeto
        fulano.setIdade(obterIdade);
        fulano.setNome(obterNome);

        // exibir os dados do objeto Valter
        System.out.println("Exibindo dados do Valter");
        System.out.println("Nome: " + valter.getNome());
        System.out.println("Idade: " + valter.getIdade());

        // exibir dados do objeto Fulano
        System.out.println();
        System.out.println("Exibindo dados do usuário");
        System.out.println("Nome: " + fulano.getNome());
        System.out.println("Idade: " + fulano.getIdade());

        scanner.close();
    }
}
