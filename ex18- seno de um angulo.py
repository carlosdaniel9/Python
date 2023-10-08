import math  # se impoprtar somente o sin, o cos e o tan, nao precida colocar o math na hora de 
# chamar as funcões nas variaveis abaixo.
angulo = float(input('Digite o angulo que você deseja!'))
seno = math.sin(math.radians(angulo))
print('O angulo de {} tem o seno {:.2f}'.format(angulo, seno))
cosseno = math.cos(math.radians(angulo))
print('O angulo de {} tem o cosseno {:.2f}'.format(angulo, cosseno))
tangente = math.tan(math.radians(angulo))
print('O angulo de {} tem o tangente {:.2f}'.format(angulo, tangente))


# carlos daniel  10/09/2023