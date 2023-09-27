# estruturas condicionais
# método padrão
tempo = int(input('Qauntos anos tem seu carro? '))
if tempo <= 3:
    print('Carro novo')
else:
    print('Carro velho')

# método simplificado

print('Carro novo'if tempo <=5 else'carro velho')
# printa carro novo se tempo for menor ou igual a 5, senão printa carro velho.