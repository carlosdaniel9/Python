import tkinter as tk

def calcular_soma():
    num1 = float(entrada1.get())
    num2 = float(entrada2.get())
    resultado.set(f"Resultado: {num1 + num2}")

# Cria uma janela
janela = tk.Tk()
janela.title("Calculadora de Soma")

# Cria as entradas de números
tk.Label(janela, text="Número 1:").pack()
entrada1 = tk.Entry(janela)
entrada1.pack()

tk.Label(janela, text="Número 2:").pack()
entrada2 = tk.Entry(janela)
entrada2.pack()

# Variável para armazenar o resultado
resultado = tk.StringVar()

# Botão para calcular a soma
botao_calcular = tk.Button(janela, text="Calcular Soma", command=calcular_soma)
botao_calcular.pack()

# Exibe o resultado
resultado_label = tk.Label(janela, textvariable=resultado)
resultado_label.pack()

# Inicia a interface gráfica
janela.mainloop()
