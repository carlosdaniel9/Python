# ira sortear os nomes adicionados nas variaveis
import random

print('Digite os nomes dos alunos')
aluno1 = input('Primeiro aluno: ')
aluno2 = input('segundo aluno: ')
aluno3 = input('terceiro aluno: ')
aluno4 = input('quarto aluno: ')

lista = [aluno1, aluno2, aluno3, aluno4]  # essa lista  esta recebendo todas as variaveis
sorteio = random.choice(lista) # a função choice da biblioteca random, ira escolher a das var da lista
print('O aluno sorteado é {}'.format(sorteio))


# carlos daniel  16/09/2023