import math  # aqui esta importando a biblioteca completa 

num = int(input('Digite um número!')) 
raiz = math.sqrt(num)  

print('A raiz quadrada de {} é igual a {:.2f}'.format(num, raiz)) # com formatação igual usa para dinheiro :.2f entre as chaves
print('A raiz quadrada de {} é igual a {}'.format(num, math.floor(raiz)))  # math.floor vai arredondar o numero para baixo
print('A raiz quadrada de {} é igual a {}'.format(num, math.ceil(raiz)))  # math.ceil vai arredondar o numero para cima 