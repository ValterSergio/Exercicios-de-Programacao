using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Exe01_PRL_080825
{
    internal class Program
    {
        static void Main(string[] args)
        {
            /*
             * Algoritmo: Encontre o Vizinho
             * 
             * Elabore um programa que leia um número. Calcule e informe os seus vizinhos, ou seja,
             * o numero anterior e o posterior
             * Exemplo:
             *  Digite um número inteiro: 15
             *  Vizinhos encontrados: 14 e 16
             * 
             * Aluno: Valter Sérgio Ribeiro Tertuliano
             * 
             */

            // VAR'S
            string entrada; 
            int numero;
            int sucessor;
            int anterior;

            // Inicio

            // Entrada
            Console.WriteLine("Digite um número: ");
            Console.SetCursorPosition(18, 0);
            entrada = Console.ReadLine();
            
            // Processsamento
            numero = int.Parse(entrada);
            sucessor = numero + 1;
            anterior = numero - 1;

            // Saída
            Console.WriteLine("Vizinhos encontrados: " + anterior + " e " + sucessor);

            // Fim
        }
    }
}
