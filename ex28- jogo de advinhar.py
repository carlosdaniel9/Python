from time import sleep
import random
print('\33[35;41m-=-\33[m'*20) # vai aparecer -=- 20 vezes .
print('       \33[0;31mEstou pensando em um número, tente adivinhar!\33[m')
print('\33[35;41m-=-\33[m'*20)
num = int(random.uniform(0, 10)) # vai selecionar um numero de 1 até 10.
num2 = int(input('Escolha um número de 0 a 10: '))
print('Processando...')
sleep(3) # vai da uma pausa no progama por 3 segundos.
if num2 == num: # se o número digitado pelo usuario for igual o num, regardo pera random da var.
    print('\33[32mVocê acertou!')
    print('Seu número foi {}, e o gerado pelo computador foi {}'.format(num2, num))
    print('Parabéns')
else:
    print('\33[31mVocê não acertou!')
    print('Seu número foi {}, e o gerado pelo computador foi {}'.format(num2, num))