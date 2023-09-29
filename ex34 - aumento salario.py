salario = float(input('Digite seu salario R$: '))
if salario <= 1250: # se salario for menor ou igual a 1250. 
    cal1 = salario + (salario * 15/100)
    print('Com seu aumento de 15% , seu salario sai de R${:.2f} para R${:.2f}'.format(salario, cal1))
else: # se-não.
    cal1 = salario + (salario * 10/100)
    print('Com seu aumento de 10% , seu salario sai de R${:.2f} para R${:.2f}'.format(salario, cal1))

    # carlos daniel     29/09/2023