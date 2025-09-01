using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Exe6_310825
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int n = 100;

            long soma_quadrados = (n * (n + 1) * (2 * n + 1)) / 6;

            long soma = (n * (n + 1)) / 2;
            long quadrado_da_soma = soma * soma;

            long diferenca = quadrado_da_soma - soma_quadrados;

            Console.WriteLine($"Soma dos quadrados: {soma_quadrados:N0}");
            Console.WriteLine($"Quadrado da soma: {quadrado_da_soma:N0}");
            Console.WriteLine($"Diferença: {diferenca:N0}");
        }
    }
}
