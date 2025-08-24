using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Exe05_PRL_23082025
{
    internal class Program
    {
        /*
         * Elabore um programa para ler uma temperatura 
         * na escala celsius e exibir o equivalente em 
         * Farenheit.
         * 
         */

        static void Main(string[] args)
        {
            double fahrenheit;
            double celsius;

            // entrada
            Console.Clear();
            Console.WriteLine("Informe a temperatura em Celsius: ");
            Console.SetCursorPosition(35, 0);
            celsius = double.Parse(Console.ReadLine());

            // processamento
            fahrenheit = 1.8 * celsius + 32;

            //saida
            Console.WriteLine("Temperatura em FAHRENHEINT: " + fahrenheit);

        }
    }
}
