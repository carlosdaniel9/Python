from math import sqrt, ceil, floor # esta importando só a funcionalidade sqrt e ceil 
# esta importando somentas as funções que desejo a biblioteca math 

num = int(input('Digite um número!'))
raiz = sqrt(num)

print('A raiz quadrada de {} é {} sem arredondamento'.format(num, raiz)) # normal sem arredondamento  
print('A raiz quadrada de {} é {} com arredondamento para baixo'.format(num, floor(raiz))) # arredondando para baixo 
print('A raiz quadrada de {} é {} com arredondamento para cima'.format(num, ceil(raiz)))  # arredondando para cima

