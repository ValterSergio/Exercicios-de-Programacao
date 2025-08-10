using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Exe04_PRL_090825
{
    internal class Program
    {
        static void Main(string[] args)
        {
            /*
             * Elabore um programa que leia 2 notas de um aluno em uma 
             * disciplina. Calcule e informe a média das notas.
             * 
             * Aluno: Valter Sérgio Ribeiro tertuliano
             */

            // Variaveis
            double nota1;
            double nota2;
            double media;

            // entrada
            Console.WriteLine("Informe a 1° nota: ");
            Console.SetCursorPosition(19, 0);
            nota1 = double.Parse(Console.ReadLine());
            Console.Clear();

            Console.WriteLine("Informe a 2° nota: ");
            Console.SetCursorPosition(19, 0);
            nota2 = double.Parse(Console.ReadLine());
            Console.Clear();

            // processamento
            media = (nota1 + nota2) / 2;

            // saida
            Console.WriteLine("1° Nota: " + nota1);
            Console.WriteLine("2° Nota: " + nota2);
            Console.WriteLine("Média do aluno(a): " + media);

        }

    }
}
