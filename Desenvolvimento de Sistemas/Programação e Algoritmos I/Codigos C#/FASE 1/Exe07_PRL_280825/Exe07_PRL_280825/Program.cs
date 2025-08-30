using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Exe07_PRL_280825
{
    internal class Program
    {
        static void Main(string[] args)
        {
            // Variaveis
            double num1;
            double num2;
            double soma;
            double produto;
            double quadrado;

            // entradas
            num1 = obter_double("Digite o 1° valor: ");
            num2 = obter_double("Digite o 2° valor: ");

            // processamento
            soma = (num1 + num2) * 0.2;
            produto = (num1 * num2) * 0.3;
            quadrado = (Math.Pow(num1, 2) + Math.Pow(num2, 2)) * 0.4;

            // saida
            Console.WriteLine($"20% da soma: {soma}");
            Console.WriteLine($"30% do produto: {produto}");
            Console.WriteLine($"40% da soma dos quadrados: {quadrado}");
        }

        static double obter_double(string mensagem)
        {
            while (true)
            {
                try
                {
                    Console.Clear();
                    Console.WriteLine("Informe Apenas números !!!");
                    Console.WriteLine(mensagem);
                    Console.SetCursorPosition(mensagem.Length, 1);
                    return double.Parse(Console.ReadLine());
                }
                catch (Exception e)
                {
                    Console.WriteLine(e.ToString());
                    continue;
                }
            }
        }
    }
}
