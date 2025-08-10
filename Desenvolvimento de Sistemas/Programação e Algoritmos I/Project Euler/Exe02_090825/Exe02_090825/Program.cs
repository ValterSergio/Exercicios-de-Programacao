using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Exe02_090825
{
    internal class Program
    {
        static void Main(string[] args)
        {
            /*
             * Cada novo termo na sequência de Fibonacci é gerado pela adição dos 
             * dois anteriores. Começando com 1 e 2, os primeiros 10 termos serão
             * 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
             * 
             * Considerando os termos na sequência de Fibonacci cujos valores não
             * excedem quatro milhões, encontre a soma dos termos de valor par.
             * 
             * Aluno: Valter Sérgio Ribeiro Tertuliano
             */

            // constantes
            const int limite_fibonacci = 4000000;

            // variaveis
            int termo1 = 0;
            int termo2 = 1;
            int fibonacci = 0;
            int total = 0;


            while (fibonacci < limite_fibonacci)
            {
                // o proximo termo de fibonacci é soma dos dois ultimos termos
                fibonacci = termo1 + termo2;

                // o primeiro termo recebe o valor do segundo termo
                termo1 = termo2;

                // o segundo termo recebe o valor de fibonnaci
                termo2 = fibonacci;

                // se o termo for par
                if (fibonacci % 2  == 0)
                {
                    // soma o termo 
                    total += fibonacci;
                }

            }
            Console.WriteLine("A soma dos termos pares de fibonacci até o limite de " + limite_fibonacci + ".");
            Console.WriteLine("Resultado: " + total);
        }
    }
}
