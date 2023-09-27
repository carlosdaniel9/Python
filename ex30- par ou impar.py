#  método 1 - usando uma função
def verificar_par_impar(numero):
    if numero % 2 == 0: # % 2 é o resto da divisão 
        return "O número {} é par.".format(numero)
    else:
        return "O número {} é ímpar.".format(numero)
numero = int(input("Digite um número inteiro: "))
resultado = verificar_par_impar(numero)
print(resultado)

# método 2 
num = int(input('Digite um número: '))
resultado2 = num % 2
if resultado2 == 0:
    print('O número {} é par'.format(num))
else:
    print('O número {} é impar'.format(num))