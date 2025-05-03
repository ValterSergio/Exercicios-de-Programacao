import java.util.Scanner;

public class Exercicio08_IdadeCategoria {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Solicita a idade
        System.out.print("Digite a idade: ");
        int idade = scanner.nextInt();

        // Classifica a idade por categoria
        if (idade >= 0 && idade <= 12) {
            System.out.println("Categoria: Criança ");
        } else if (idade >= 13 && idade <= 17) {
            System.out.println("Categoria: Adolescente ");
        } else if (idade >= 18 && idade <= 59) {
            System.out.println("Categoria: Adulto");
        } else if (idade >= 60) {
            System.out.println("Categoria: Idoso ");
        } else {
            System.out.println("Idade inválida. ");
        }

        // Fecha o scanner
        scanner.close();
    }
}
