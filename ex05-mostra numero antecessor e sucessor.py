# entra com um numero, e saber qual numero vem antes e depois dele.

num1 = int(input('digite um numero')) # o input, está converteno para numero int, e mandando o valor para a var num1
antesesor = num1 - 1   # a var antensesor, pega o valor da num1,e diminu 1 
susesor = num1 +1      # a var susesor , pega o valor de num, e soma com 1 

# printando no terminal as variaveis, usandoo .format  | o \n serve para da quebra de linha.
print('analisando o numero {}, \n seu susessor é {}, \n seu antesessor é {}'.format(num1,antesesor,susesor))