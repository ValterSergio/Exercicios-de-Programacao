using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Exe7_310825
{
    internal class Program
    {
        static void Main(string[] args)

        {
            long n = 10001;
            Console.WriteLine($"O {n:N0}° é {EncontrarEnesimoPrimo(n):N0}");
        }

        static long EncontrarEnesimoPrimo(long n)
        {
            long num = 1;
            long cont = 0;

            while (cont < n)
            {
                num++;
                if (ValidarPrimo(num))
                {
                    cont++;
                }
                
            }
            return num;
        }

        static bool ValidarPrimo(long n)
        {
            if (n < 2) {  return false; }
            if (n == 2) { return true; }
            if (n % 2 == 0) { return false; };
            

            long i = 3;

            while (i * i <= n) 
            {
                if (n % i  == 0) { return false; }
                i += 2;
            }
            return true;

        }
    }
}
