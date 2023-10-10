# variavel, bin(variavel) | vai converter o numero da variavel para binário.
# variavel, oct(variavel) | vai converter o numero da variavel para octal.
# variavel, hex(variavel) | vai converter o numero da variavel para hexadecimal.
num = int(input('digite um número inteiro: '))
print(''' Escolha uma das bases para conversão:
    [1] converter para BINÁRIO
    [2] converter para OCTAL
    [3] converter para HEXADECIMAL''')

opcao = int(input('Sua opção: '))

if opcao == 1:
    print('{} convertido para BINARIO é igual a {}'.format(num, bin(num)[2:])) # o [2:], siginifica que vai mostrar apartir do terceiro caracter, ja que começa a contagem de 0.
elif opcao == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção invalida') 




# carlos daniel      09/10/2023