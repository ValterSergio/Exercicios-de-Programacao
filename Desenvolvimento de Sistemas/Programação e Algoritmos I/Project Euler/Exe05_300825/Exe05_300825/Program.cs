using System;

namespace Exe05_300825
{
    internal class Program
    {
        /*
         * Aplicação de força bruta
         * 
         * 2520 é o menor numero que pode ser dividido por cada um dos numeros de 1 a 10 sem qualquer resto.
         * Qual é o menor número positivo que é uniformemente divisível por todos os números de 1 a 20?
         */
        static void Main(string[] args)
        {
            int[] numeros_para_testar = GerarNumeros(22);
            int numero_alvo = 20;

            while (true)
            {
                int contar = 0;
                for (int i = 0; i < numeros_para_testar.Length; i++)
                {
                    if (numero_alvo % numeros_para_testar[i] == 0)
                    {
                        contar++;
                    }
                    else
                    {
                        break; // se não dividir por um, não precisa testar os outros
                    }
                }

                if (contar == numeros_para_testar.Length)
                {
                    break;
                }

                numero_alvo++;
            }

            Console.WriteLine("N: " + numero_alvo);
        }

        static int[] GerarNumeros(int n)
        {
            int[] vetor = new int[n - 1];
            for (int i = 0; i < n - 1; i++)
            {
                vetor[i] = i + 2;
            }
            return vetor;
        }
    }
}
