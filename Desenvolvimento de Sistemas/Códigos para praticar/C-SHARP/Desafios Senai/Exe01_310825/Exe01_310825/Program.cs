using System;

namespace Exe01_310825
{
    internal class Program
    {
        static void Main(string[] args)
        {
            // VAR
            double salarioBase;
            double salarioFinal;
            int tempoServico;
            int notaDesempenho;
            int bonusRecebido;

            // Entrada
            salarioBase = ObterSalarioBase();
            tempoServico = ObterTempoServico();
            notaDesempenho = ObterNotaDesempenho();

            // processamento
            bonusRecebido = CalcularBonus(tempoServico, notaDesempenho);
            salarioFinal = CalcularSalarioFinal(bonusRecebido, salarioBase);

            // saida
            Console.WriteLine($"Salario Base: {salarioBase:C2}");
            Console.WriteLine($"Bônus recebido: {bonusRecebido}%");
            Console.WriteLine($"Salario Final: {salarioFinal:C2}");
        }

        static double CalcularSalarioFinal(int bonus, double salario)
        {
            return salario + (salario * (bonus / 100.0));
        }
        static int CalcularBonus(int tempo, int nota)
        {
            int bonus;
            if (tempo < 3)
            {
                Console.WriteLine("\nTempo de servico Insuficiente para bonus");
                bonus = 0;
            } else if (tempo >= 3 && tempo <= 5)
            {
                Console.WriteLine("\nBonus por tempo de servico: 5%");
                bonus = 5;
            } else
            {
                Console.WriteLine("\nBonus por tempo de servico: 10%");
                bonus = 10;
            }
            if (nota < 4)
            {
                Console.WriteLine("\nDesempenho muito Baixo: Bonus anulado");
                bonus = 0;
            }
            else if (nota >= 4 && nota <= 7)
            {
                Console.WriteLine("Desempenho mediano: Bonus inalterado: " + bonus + "%\n");
            }
            else
            {
                bonus = bonus * 2;
                Console.WriteLine("Desempenho Excelente: Bonus dobrado: " + bonus + "%\n");
            }
            return bonus;

        }

        static int ObterNotaDesempenho()
        {
            // entrada
            int nota;
            Console.Clear();
            string msg = "Informe a nota de desempenho: ";
            Console.WriteLine(msg);
            Console.SetCursorPosition(msg.Length, 0);
            nota = int.Parse(Console.ReadLine());

            if (nota >= 0 && nota <= 10)
            {
                return nota;
            } else
            {
                Console.WriteLine("ERRO: Informe Apenas valores no intervalo de 0-10 !!!\n");
                Environment.Exit(0);
                return -1;
            }   
        }
        static int ObterTempoServico()
        {
            // entrada
            int tempo;
            Console.Clear();
            string msg = "Informe o tempo de serviço: ";
            Console.WriteLine(msg);
            Console.SetCursorPosition(msg.Length, 0);
            tempo = int.Parse(Console.ReadLine());

            if (tempo > 0)
            {
                return tempo;
            } else
            {
                Console.WriteLine("ERRO: Informe Apenas valores inteiros positivos\n");
                Environment.Exit(0);
                return -1;
            }

        }
        static double ObterSalarioBase()
        {
            // entrada
            double salario;
            Console.Clear();
            string msg = "Informe o salário base: ";
            Console.WriteLine(msg);
            Console.SetCursorPosition(msg.Length, 0);
            salario = double.Parse(Console.ReadLine());

            // validar entrada
            if (salario > 0)
            {
                return salario;
            }
            else
            {
                Console.WriteLine("ERRO: Informe apenas valores Positivos\n");
                Environment.Exit(0);
                return -1;
            }
        }
    }
}
