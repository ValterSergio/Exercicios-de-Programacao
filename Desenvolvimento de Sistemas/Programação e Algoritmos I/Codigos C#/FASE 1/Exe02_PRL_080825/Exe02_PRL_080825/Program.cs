using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Exe02_PRL_080825
{
    internal class Program
    {
        static void Main(string[] args)
        {
            /*
             * Elaborar um programa para uma pizzaria, o qual o valor total
             * de uma conta e quantos cliente vão pagá-la. Calcule o valor 
             * pago por cliente.
             * 
             * Exemplo:
             *      Digite o valor da conta R$: 120.00
             *      Quantidade de clientes: 3
             *      Valor por cliente: R$: 40.00
             *  
             * Aluno: Valter Sérgio Ribeiro Tertuliano
             */

            // Variaveis
            double conta;
            int clientes;
            double total;

            // entrada
            Console.WriteLine("Informe o valor total da conta: ");
            Console.SetCursorPosition(32, 0);
            string valor_conta = Console.ReadLine();
            Console.Clear();
            Console.SetCursorPosition(0, 0);


            Console.WriteLine("Informe o total de clientes: ");
            Console.SetCursorPosition(29, 0);
            string total_clientes = Console.ReadLine();
            Console.Clear();

            // Processamento
            conta = double.Parse(valor_conta);
            clientes = int.Parse(total_clientes);
            total = conta / clientes;

            // Saída
            Console.WriteLine("Valor da conta: " + conta);
            Console.WriteLine("Total de clientes: " + clientes);
            Console.WriteLine("Valor por cliente: " + total);
            
            // Fim
        }
    }
}
