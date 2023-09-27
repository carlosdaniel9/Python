frase = str(input('Digite uma frase: ')).upper().strip() 
print('A letra A aparece {} vezes em sua frase'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A') + 1))
# o find vai encontra a primeira letra na frase da esquerda para direita, o +1 vai adequar pois no python, começa no 0
# assim deixara a contagem começando no 1, como nós usamos geralmente no dia a dias.
print('A ultima letra A aparece na posição {}'.format(frase.rfind('A'))) # o rfind vai começar a procurar da direita para eesquerda