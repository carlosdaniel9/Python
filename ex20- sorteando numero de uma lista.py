from random import shuffle # importando a função shuffle da biblioteca random
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))

lista = [n1, n2, n3, n4]
shuffle(lista) # o shuffle embaralha a lista
print('A ordem da lista será de forma aleatoria:')
print(lista)


# carlos daniel  20/09/2023