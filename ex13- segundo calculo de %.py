salario = float(input('Digite seu salario!'))
aumento = salario + (salario * 15/100)

print('Você ganhava R${}, com aumento de 15%, você passa a ganha R${:.2f}'.format(salario, aumento))