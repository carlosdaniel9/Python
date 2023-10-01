km = int(input('Qual a velocidade do carro? '))
cores = {'azul':'\033[34m', 'fechamento':'\033[m', 'vermelho':'\033[31m'}  # variavel com cores
valor_Multa_Km = 7 
cal = (km - 80) * valor_Multa_Km  # vai fazer o calculo apenas do que passar de 80, vezes 7 que é o valor por KM
if km <= 80:
    print('{}Sua velocidade é {} Km/h'.format(cores['azul'], km)) # como não estou usando a fechamento
    print('Tenha um bom dia, diriga com segurança')               # ele vai colorir de azul os 2 prints.
else:
    print('Sua velocidade é {} Km/h'.format(km))
    print('Você ultrapassou o limite de velocidade')
    print('{}MUlTADO, você deve pagar R${:.2f}{}'.format(cores['vermelho'], cal, cores['fechamento']))
    # a primeira {}, está recebendo cores['vermelho'] a segunda {} é a variavel, e a terceira {} a cores['fechamento']


    # carlos daniel    28/09/2023