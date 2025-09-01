using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Exe05a_300825
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int limite = 50;
            long resultado = 1;

            for (int i = 2; i <= limite; i++) 
            {
                resultado = MMC(resultado, i);
            }

            Console.WriteLine($"O menor numero divisilvel: {resultado:N0}");
        }

        static long MDC(long a, long b)
        {
            while (b != 0)
            {
                long temp = b;
                b = a % b;
                a = temp;
            }
            return a;

        }

        static long MMC(long a, long b)
        {
            return (a * b) / MDC(a, b);
        }
    }
}
