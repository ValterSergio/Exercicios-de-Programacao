using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Exe01
{
    internal class Program
    {
        static void Main(string[] args)
        {
            // somar os tempos 
            int tempo = 0;
            string tempoAtual = "";
            int media = 0;

            for (int i = 0; i < 3; i++)
            {
                tempoAtual = ColetarTempo();

                // verifica se é um numero inteiro
                if (!ValidarTempoInteiro(tempoAtual))
                {
                    Console.WriteLine("Informe apenas números inteiros");
                    break;
                }

                // converte a entrada para um número inteiro
                int tempoPositivo = int.Parse(tempoAtual);

                // verifica se é um numero positivo
                if (!ValidarTempoPositivo(tempoPositivo))
                {
                    Console.WriteLine("Informe apenas número maior que ZERO.");
                    break;
                }

                tempo += tempoPositivo;
                }

            // a média é o valor dos tempos dividido por 3
            media = tempo / 3;
            ExibirResultado(media);

            }

        public static void ExibirResultado(int media)
        {
            Console.Clear();
            Console.WriteLine("Analisando Resultado do atleta\n");
            if (media <= 10)
            {
                Console.WriteLine("Atleta categoria OURO !!");
                Console.WriteLine("Média conquistada: " +  media);
            } else if (media > 10 && media <= 15)
            {
                Console.WriteLine("Atleta categoria PRATA !!");
                Console.WriteLine("Média conquistada: " + media);
            } else if (media > 15 && media <= 20)
            {
                Console.WriteLine("Atleta categoria BRONZE !!");
                Console.WriteLine("Média conquistada: " + media);
            } else
            {
                Console.WriteLine("Atleta DESCLASSIFICADO !!");
                Console.WriteLine("Média conquistada: " + media);
            }
        }

        public static string ColetarTempo()
        {
            string texto = "Informe o tempo do atleta: ";
            Console.Clear();
            Console.WriteLine(texto);
            Console.SetCursorPosition(texto.Length + 1, 0);
            return Console.ReadLine();
        }

        public static bool ValidarTempoInteiro(string tempo)
        {
            // verifica se o valor digitado é um numero inteiro
            if (int.TryParse(tempo, out int inteiro))
            {
                return true;
            } else
            {
                return false;
            }

        }
        public static bool ValidarTempoPositivo(int tempo)
        {
            return tempo > 0;
            
        }
    }
}