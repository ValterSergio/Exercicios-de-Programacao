using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Exe02
{
    internal class Program
    {
        static void Main(string[] args)
        {
            // VAR
            double salario;
            int tempoServico;
            int notaDesempenho;


            // INICIO
            salario = ObterSalario();
            tempoServico = ObterTempoDeServico();
            notaDesempenho = ObterNotaDeDesempenho();

            // PROCESSAMENTO
            bool continuarPrograma = EncontrarErro(salario, tempoServico, notaDesempenho);
            if (continuarPrograma)
            {
                // saida
                ExibirResultado(salario, tempoServico, notaDesempenho);
            }
            else
            {
                // saida
                Console.WriteLine("Tente Novamente: erro indentificado");
            }
        }

        public static bool EncontrarErro(double salario, int tempoServico, int notaDesempenho)
        {
            if (ValidarPositivo(salario) && ValidarPositivo(tempoServico) && ValidarPositivo(notaDesempenho))
            {
                // se todos são positivos não teve retorno 0 como sinal de erro
                return true;
            } else
            {
                return false;
            }
        }

        public static void ExibirResultado(double salario, int tempoServico, int notaDesempenho)
        {
            int bonus = 0;
            double novoSalario;
            Console.Clear();

            // calcula bonus por tempo de servico
            if (tempoServico < 3)
            {
                Console.WriteLine("Sem bonus por tempo de serviço.");
                bonus = 0;
            } else if (tempoServico >= 3 && tempoServico <= 5)
            {
                Console.WriteLine("Bonus de 5% por tempo de serviço.");
                bonus = 5;
            } else
            {
                Console.WriteLine("Bonus de 10% por tempo de serviço");
                bonus = 10;
            }

            // calcula nota de desempenho e incrementa o bonus
            if (notaDesempenho < 4)
            {
                Console.WriteLine("Bonus perdido por baixo desempenho");
                bonus = 0;

            } else if (notaDesempenho >= 4 && notaDesempenho <= 7)
            {
                Console.WriteLine("Bonus Inalterado por desempenho mediano");
            } else if (notaDesempenho > 7)
            {
                Console.WriteLine("Bonus dobrado por bom desempenho");
                bonus *= 2;
            }

            if (bonus > 0)
            { 
                Console.WriteLine("Bonus Atual: " + bonus + "%");
                novoSalario = salario * (1 + (bonus / 100.0));
                Console.WriteLine("Salario atualizado: R$ " + novoSalario);
            }
            else
            {
                Console.WriteLine("Sem direito a bonus.");
                Console.WriteLine("Salario atual: R$ " + salario);

            }


        }
        public static int ObterNotaDeDesempenho()
        {
            int desempenho = 0;
            string texto = "Informe a nota de desempenho (0 a 10): ";
            Console.Clear();
            Console.WriteLine(texto);
            Console.SetCursorPosition(texto.Length + 1, 0);
            string nota = Console.ReadLine();

            Console.WriteLine("\nValidando Nota de Desempenho\n");
            // é um inteiro
            if (ValidarInteiro(nota))
            {

                desempenho = int.Parse(nota);
                // é positivo
                if (ValidarPositivo(desempenho))
                {
                    // é maior que zero e menor que 10?
                    if (desempenho > 0 && desempenho <= 10)
                    {
                        Console.WriteLine("Nota de desempenho válidada");
                    }
                    else
                    {
                        Console.WriteLine("Erro: A nota deve estar entre 1 e 10.");
                    }
                }
                else
                {
                    Console.WriteLine("ERRO: Informe apenas valores positivos.");
                }
            } else
            {
                Console.WriteLine("ERRO: Informe apenas numeros inteiro.");
            }
            return desempenho;

        }
        public static int ObterTempoDeServico()
        {
            int tempo = 0;

            string texto = "Informe o tempo de serviço em anos: ";
            Console.Clear();
            Console.WriteLine(texto);
            Console.SetCursorPosition(texto.Length + 1, 0);
            string salario = Console.ReadLine();

            Console.WriteLine("Validando Tempo de serviço.");
            // verifica se o número é um inteiro
            if (ValidarInteiro(salario))
            {
                tempo = int.Parse(salario);
                if (ValidarPositivo(tempo))
                {
                    Console.WriteLine("Tempo de serviço válidado.");
                }
                else
                {
                    Console.WriteLine("ERRO: Informe apenas numeros positivos");
                }
            }
            else
            {
                Console.WriteLine("ERRO: Informe apenas Números Inteiros");
            }
            return tempo;
        }
        public static double ObterSalario() 
        {
            double salarioBase = 0;
            
            // entrada do usuario
            string texto = "Informe o salario base: ";
            Console.Clear();
            Console.WriteLine(texto);
            Console.SetCursorPosition(texto.Length + 1, 0);
            string salario = Console.ReadLine();

            Console.WriteLine("Validando Salario");

            // processar entrada
            if (ValidarReal(salario))
            {
                salarioBase = double.Parse(salario);

                if (ValidarPositivo(salarioBase))
                {
                    Console.WriteLine("Salario Válidado");

                }
                else
                {
                    Console.WriteLine("ERRO: Informe apenas números positivos");
                }
            } else
            {
                Console.WriteLine("ERRO: Informe apenas números Inteiros");
            }
            return salarioBase;
        }

        // metodos para validar numeros positivos, inteiros e reais
        public static bool ValidarPositivo(int n) 
        {
            return n > 0;
        }

        public static bool ValidarPositivo(double n)
        {
            return n > 0;
        }

        public static bool ValidarInteiro(string n)
        {
            Console.Clear();
            Console.WriteLine("Verificando número !!!\n");
            if (int.TryParse(n, out int resultado))
            {
                Console.WriteLine("Número Válidado");
                return true;
            } else
            {
                Console.WriteLine("Número Inválido, informe apenas número inteiros");
                return false;
            }
        }
        public static bool ValidarReal(string n)
        {
            Console.Clear();
            Console.WriteLine("Verificando número !!!\n");
            if (double.TryParse(n, out double resultado))
            {
                Console.WriteLine("Número Válidado");
                return true;
            }
            else
            {
                Console.WriteLine("Número Inválido, informe apenas números");
                return false;
            }
        }

    }
}