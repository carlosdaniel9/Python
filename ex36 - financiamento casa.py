valorCasa = float(input('Digite o valor da casa:'))
salario = float(input('Qual seu salario? '))
anos = int(input('Em quantos anos você pretende paga a casa: '))   

# vai da quantos mês ira levar para paga a casa .
cal = anos * 12 # quantidade de anos, vezes 12 meses de cada ano.

# vai dividir o valor da casa pela quantidade de mês, que vai da o valor da parcela por mês.
prestacao = valorCasa / cal

# vai calcular o valor de 30% do salario 
minimo = (salario * 30/100)

# se cal2(os 30% do salário) for menor que cal1(valor das parcelas mensais), printa que foi aprovado, e as demias mensagens.
if minimo >= prestacao :
    print('Financiamento aprovado, o valor da parcela e menor que 30% do seu salario')
    print('30% do seu salario é: R${} '.format(minimo))
    print('A casa de R${:.2f}, parcelada  em {:.0f} vezes, você pagara R${:.2f} mensalmente'.format(valorCasa, cal, prestacao))
else:  # se não, printa que foi negado, pois o valor dos 30% e inferior ao valor a ser pago mensalmente.
    print('Financiamento negado, o valor da parcela ultrapassa 30% do seu salario')
    print('30% do seu salario é: {:.2f}, não é suficiente para pagar uma parcela de R${:.2f} mensais'.format(minimo, prestacao))





# carlos daniel        09/10/2023