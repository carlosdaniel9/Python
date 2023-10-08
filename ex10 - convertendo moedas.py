saldo = float(input('Quanto você ten na carteira R$ '))
dolar = 4.89                 # valor do dolar em 27/08/2023 as 22 hrs
converte = saldo / dolar    # a var converte esta pegando, o valor da variavel saldo
                            # e dividindo pela variavel dolar, que vale 4.89

print('voce tem R$ {}, e você pode compra US$ {:.2f}'.format(saldo, converte))

# convertendo real para euro 
saldo2 = float(input('Quantos você quer converter para EURO?'))
euro = 5.28
converter2 = saldo2 / euro

print('com {}, você pode comprar {:.2f} euro'.format(saldo2, converter2))

# carlos daniel   27/08/2023