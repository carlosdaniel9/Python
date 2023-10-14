from time import sleep
from random import randint
itens = ('pedra', 'papel', 'tesoura')
computador = randint(0, 2)
print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA
''')
jogador = int(input('Qual é sua jogada? '))

print(14 * '-=')
print('Você jogou {}'.format(itens[jogador])) # vai mostar a escolha do jogador
print('O computador jogou {}'.format(itens[computador])) # vai mostra a escolha do computador
print(14 * '-=')

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('Po!!!')

if computador == 0: # se o computador jogar pedra
    if jogador == 0:
        print('EMPATE')
    elif jogador ==1:
        print('VOCÊ VENCEU')
    elif jogador ==2:
        print('COMPUTADOR GANHOU')
elif computador == 1: # se o computador jogar papel
    if jogador == 0:
        print('COMPUTADOR GANHOU')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('VOCÊ GANHOU')
elif computador ==2: # se o computador jogar tesoura
    if jogador == 0:
        print('VOCÊ GANHOU')
    elif jogador == 1:
        print('COMPUTADOR GANHOU')
    elif jogador == 2:
        print('EMPATE')



# carlos daniel    14/10/2023