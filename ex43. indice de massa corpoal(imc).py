peso = float(input('Qual é seu peso? (Kg)'))
altura = float(input('Qual é sua altura? (m)'))
imc = peso / (altura ** 2)
print('Seu imc é {:.1f}'.format(imc))
if imc < 18.5:
    print('Abaixo do peso')
elif imc < 25:
    print('Peso ideal')
elif imc < 30:
    print('Sobrepeso')
elif imc < 40:
    print('Obesidade')
else: # nesse caso estou usando o else, pois se não for nenhum dos teste acima, vai ser acima de 40 o ims, então sera obesidade mórbida
    # mais poderia usar o elif também, com o teste se elif imc > 40: (imc for maior que 40.)
    print('Obesidade mórbida')




# carlos daniel    13/10/2023