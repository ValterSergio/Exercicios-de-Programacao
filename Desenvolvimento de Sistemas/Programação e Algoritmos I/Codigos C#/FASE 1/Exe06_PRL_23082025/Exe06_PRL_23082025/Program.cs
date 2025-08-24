using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Exe06_PRL_23082025
{
    internal class Program
    {
        /*
         * Elabore um programa que receba dois valores e calcule:
         * 1) 20% da soma
         * 2) 30% do produto
         * 3) 40% das soma dos quadrados
         * 
         */

        static void Main(string[] args)
        {
            double num1, num2, soma, produto, quadrado;

            // Entrada
            num1 = obter_num_real(1);
            num2 = obter_num_real(2);

            // Processamento
            soma = obterPorcentagem(0.2, (num1 + num2));
            produto = obterPorcentagem(0.3, (num1 * num2));
            quadrado = obterPorcentagem(0.4, (Math.Pow(num1, 2) + Math.Pow(num2, 2)));

            // Saida
            Console.WriteLine("20% da Soma: " + soma);
            Console.WriteLine("30% do produto: " + produto);
            Console.WriteLine("40% da soma dos quadrados: " + quadrado);
        }

        static double obterPorcentagem(double porcentagem, double valor)
        {
            return valor * porcentagem;
        }

        static double obter_num_real(int n)
        {
            Console.Clear();
            string msg = "Informe o " + n + "° número: ";
            Console.WriteLine(msg);
            Console.SetCursorPosition(msg.Length, 0);
            return double.Parse(Console.ReadLine());
        }
    }
}
