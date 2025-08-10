using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Exe03_090825
{
    internal class Program
    {
        static void Main(string[] args)
        {
            /*
             * Os fatores primos de 13195 são 5, 7, 13 e 29
             * Qual é o maior fator primo do número 600851475143 ?
             * 
             * Aluno: Valter Sérgio Ribeiro Tertuliano
             * 
             */

            // VARIAVEIS

            // int não tem espaço suficiente
            long n = 13195;

            // Processamento
            int maiorFator = EncontrarMaiorFator(n);

            // Saida
            Console.WriteLine("O maior fator primo do número " + n + " é: " + maiorFator);

        }

        public static int EncontrarMaiorFator(long n)
        {
            // 0 e 1 são números especias e não são primos
            int fator = 2; // int deve ser suficiente

            // guardar o maior fator encontrado
            int maiorFator = 0;

            while (n > 1)
            {
                if (n % fator == 0)
                {
                    maiorFator = fator;
                    n /= fator;
                }
                else
                {
                    fator++;
                }
            }
            return maiorFator;

        }
    
        
    }
}
