using System;

class Program
{
    static void Main()
    {
        while (true)
        {
            Console.WriteLine("Escolha uma operação:");
            Console.WriteLine("1 - Adição");
            Console.WriteLine("2 - Subtração");
            Console.WriteLine("3 - Multiplicação");
            Console.WriteLine("4 - Divisão");
            Console.WriteLine("5 - Sair");

            // Lê a escolha do usuário
            int escolha = int.Parse(Console.ReadLine());

            if (escolha == 5)
            {
                // Encerra o programa se o usuário escolher sair
                break;
            }

            Console.WriteLine("Digite o primeiro número:");
            double numero1 = double.Parse(Console.ReadLine());

            Console.WriteLine("Digite o segundo número:");
            double numero2 = double.Parse(Console.ReadLine());

            double resultado = 0;

            // Realiza a operação com base na escolha do usuário
            switch (escolha)
            {
                case 1:
                    resultado = numero1 + numero2;
                    break;
                case 2:
                    resultado = numero1 - numero2;
                    break;
                case 3:
                    resultado = numero1 * numero2;
                    break;
                case 4:
                    if (numero2 != 0)
                    {
                        resultado = numero1 / numero2;
                    }
                    else
                    {
                        Console.WriteLine("Erro: Divisão por zero!");
                        continue;
                    }
                    break;
                default:
                    Console.WriteLine("Escolha inválida. Por favor, escolha uma opção válida.");
                    continue;
            }

            Console.WriteLine("Resultado: " + resultado);
        }
    }
}
