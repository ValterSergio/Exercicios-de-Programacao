using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Exe02_310825
{
    internal class Program
    {
        static void Main(string[] args)
        {
            // VAR
            string senhaCorreta = "1234";
            int tentativas = 3;
            string senhaUsuario;

            while (tentativas > 0) 
            {
                // Entrada
                senhaUsuario = ObterSenhaUsuario(tentativas);

                // comparar a senha que o usuario escreveu com a definida
                if (senhaUsuario.Equals(senhaCorreta)) 
                {
                    // se for igual libera o acesso
                    Console.WriteLine("Acesso Liberado");
                    break;

                } else 
                {
                    // se não desconta uma tentativa e tenta novamente
                    Console.WriteLine("Acesso Negado");
                    tentativas--;

                }
                
            }

        }

        static string ObterSenhaUsuario(int tentativas)
        {
            Console.Clear();
            // obter a senha do usuario
            string msg = "Informe a senha: ";
            Console.WriteLine($"Tentativas Restantes: {tentativas}");
            Console.WriteLine(msg);
            Console.SetCursorPosition(msg.Length, 1);
            return Console.ReadLine();
        }
    }
}
