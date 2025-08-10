using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Exe04_090825
{
    internal class Program
    {
        static void Main(string[] args)
        {
            /*
             * Um número palíndromo é lido da mesma forma em ambas as direções. O maior
             * palíndromo formado pelo produto de dois números com 2 digitos é 9009 (91 * 99)
             * 
             * Encontre o maior palíndromo feito do produto de dois números com 3 digitos.
             * 
             * Aluno: Valter Sérgio Ribeiro Tertuliano
             * 
             */

            // VARIAVEIS
            int numeroInicial = 100;
            int numeroFinal = 999;
            long palindromo = 0;


            // processar o resultado
            palindromo = EncontrarMaiorPalindromo(numeroInicial, numeroFinal);

            // Saída
            Console.WriteLine("\nO maior palindromo de 3 digitos encontrado: " + palindromo);
        }

        public static long EncontrarMaiorPalindromo(int numeroInicial, int numeroFinal)
        {
            // VARIAVEIS
            long produto = 0;
            long palindromo = 0;
            
            // INICIO - PROCESSAMENTO
            for (int i = numeroFinal; i >= numeroInicial; i--)
            {   

                for (int j = i; j >= numeroInicial; j--)
                {
                    produto = i * j; // i se mantem até todos os valores de j
                   
                    string produtoString = produto.ToString();
                    string inverterProduto = InverterString(produto.ToString());

                    if (inverterProduto.Equals(produtoString))
                    {
                        // verifique se é o maior palindromo
                        if (palindromo < produto)
                        {
                            palindromo = produto;
                            //Console.WriteLine("Palindromo Atual: " + palindromo + " = " + i + " * " + j);
                        }
                    }
                }
            }

            // RETORNO - RESPOSTA 
            return palindromo;
        }

        public static string InverterString(string s)
        { 
            string invertida = "";

            for (int i = s.Length - 1; i >= 0; i--)
            {
                invertida += s[i];
            }
            return invertida;
        }
    }
}
