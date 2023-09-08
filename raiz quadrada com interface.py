import tkinter as tk
from tkinter import messagebox
import math

# Função para calcular a raiz quadrada do número inserido
def calcular_raiz_quadrada():
    try:
        numero = float(entrada_numero.get())
        resultado = math.sqrt(numero)
        messagebox.showinfo("Resultado", f"A raiz quadrada de {numero} é {resultado:.2f}")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número válido.")

# Configuração da janela principal
janela = tk.Tk()
janela.title("Calculadora de Raiz Quadrada")

# Rótulo e entrada para o número
label_numero = tk.Label(janela, text="Digite um número:")
label_numero.pack()

entrada_numero = tk.Entry(janela)
entrada_numero.pack()

# Botão para calcular a raiz quadrada
botao_calcular = tk.Button(janela, text="Calcular Raiz Quadrada", command=calcular_raiz_quadrada)
botao_calcular.pack()

# Executar a interface gráfica
janela.mainloop()
