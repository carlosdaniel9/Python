print( 5 * "-=- "  + 'LOJA ONLINE'+ 5 * ' -=-')
compra = float(input('Qual o valor de sua compra? '))
print('''Escolha a forma de pagamento
[1] à vista dinheiro
[2] à vista cartão
[3] 2x no cartão
[4]3x ou mais no cartão''')
escolha = int(input('Qual a forma de pagamento? '))
if escolha == 1:
    calculo = compra - (compra * 10/100)
    print('Sua compra de R$ {:.2f} com 10% de desconto fica R$ {:.2f}'.format(compra, calculo))
elif escolha == 2:
    calculo = compra - (compra * 5/100)
    print('Sua compra de R$ {:.2f} com 5% de desconto fica R$ {:.2f}'.format(compra, calculo))
elif escolha == 3:
    parcela = compra / 2
    print('Sua compra parcelada em 2x de R$ {:.2f} ficará R$ {:.2f} no final'.format(parcela, compra))
elif escolha == 4:
    print('Sua compra parcelda em 3x ou mais vezes, tera um juro de 20% de acrescimo')
    calculo = compra + (compra * 20/100)
    totalParcela = int(input('Em quantas vezes você quer dividir sua compra? '))
    parcela = calculo / totalParcela
    print('Sua compra parcelada em {}x de R$ {:.2f}  ficará R$ {:.2f} no final'.format(totalParcela, parcela, calculo))
    
else:
    print('\033[0;31;45m Escolha um opção válida!\033[m')



# carlos daniel    13/10/2023