km = int(input('Qual a velocidade do carro? '))
valor_Multa_Km = 7
cal = (km - 80) * valor_Multa_Km  # vai fazer o calculo apenas do que passar de 80, vezes 7 que é o valor por KM
if km <= 80:
    print('Sua velocidade é {} Km/h'.format(km))
    print('Tenha um bom dia, diriga com segurança')
else:
    print('Sua velocidade é {} Km/h'.format(km))
    print('Você ultrapassou o limite de velocidade')
    print('MUlTADO, você deve pagar R${:.2f}'.format(cal))