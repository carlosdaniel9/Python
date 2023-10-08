# para colocar cores usa 
# \33[0;32;45m  primeiro numero depois do [, é o estilo, depois, cor do texto e por fim cor do fundo, e finaliza com o  m 
# para que a cor se encerrar em cada linha coloca \\33[m no final, mais dentro das aspas.
# 1- estilo | 0- sem nada | 1- em negrito | 4- texto sublinhado | 7- inverte as cores de fundo e texto
# 2- cor do texto | 30-branco | 31-vermelho | 32-verde | 33-amarelo | 34-azul | 35-rosa | 36-azul claro | 37-cinza
# 3- cor do fundo | 30-branco | 31-vermelho | 32-verde | 33-amarelo | 34-azul | 35-rosa | 36-azul claro | 37-cinza

# alguns exemplos 
print('\033[0;31;45m hello, word!\033[m')
print('\033[1;30;43m hello, word!\033[m')
print('\033[4;32m hello, word!\033[m')
print('\033[7;36;44m hello, word!\033[m')
print('\033[0;35;41m hello, word!\033[m')

# usando com o .format
nome = ('carlos')
print('seu nome é {}'.format('\033[35m', nome, '\033[m'))
