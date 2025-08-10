using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Exe01_090825
{
    internal class Program
    {
        static void Main(string[] args)
        {
            /*
             * Se listarmos todos os números naturais abaixo de 10
             * que são multiplos de 3 ou 5, nós obtemos 3, 5, 6 e 9.
             * A soma desses múltiplos é 23.
             * Encontre a soma de todos os múltimos de 3 ou 5 abaixo
             * de 1000
             * 
             * Aluno: Valter Sérgio Ribeiro Tertuliano
             */

            // variaveis
            int total = 0;

            for (int i = 0; i < 1000; i++)
            {
                if (i % 3 == 0 || i % 5 == 0) 
                { 
                    total += i;
                }
            }

            Console.WriteLine("A soma de todos os multiplos: " + total);
        }
    }
}
