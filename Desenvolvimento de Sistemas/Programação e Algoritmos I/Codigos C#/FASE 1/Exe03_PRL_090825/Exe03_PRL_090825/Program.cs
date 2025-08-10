using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Exe03_PRL_090825
{
    internal class Program
    {
        static void Main(string[] args)
        {
            /* Elaborar um programa para uma loja, o qual leia o preço de
             * um produto e informe as opções de pagamento da loja. Calcule
             * e informe o valor para pagamento a vista com 10% de desconto
             * e o valor parcelado em 3 vezes.
             * 
             * Aluno: Valter Sergio Ribeiro Tertuliano
             *
             */

            // Constantes
            const double DESCONTO = 10 / 100;
            const int PARCELAS = 3;

            // Variaveis
            double preco;
            double vista;
            double parcela;

            // entrada
            Console.WriteLine("Digite o preço do produto: ");
            Console.SetCursorPosition(27, 0);
            
            // obtem o preco com conversão direta
            preco = double.Parse(Console.ReadLine());

            // Processamento
            vista = preco * (1 -  DESCONTO);
            parcela = preco / PARCELAS;

            // saida
            
            Console.Clear(); //limpa o console
            Console.WriteLine("Valor do Produto: " + preco + " R$");
            Console.WriteLine("Valor em 3x: " + parcela + " R$");
            Console.WriteLine("Valor a Vista: " + vista + " R$");

        }
    }
}
