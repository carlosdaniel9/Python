# custo por viagem
cores = {'azul':'\033[34m', 'fechamento':'\033[m', 'vermelho':'\033[31m', 'verde':'\033[33m',} # variavel com cores
print('{}Valor de viagem{}'.format(cores['azul'], cores['fechamento']))
print('{}Até 200km fica R$ 0.50  por KM rodados{}'.format(cores['azul'], cores['fechamento']))
print('{}Acima de 200km fica R$ 0.45 por KM rodados{}\n'.format(cores['azul'], cores['fechamento']))
km = float(input('Quantos KM é sua viagem? \n'))
cal1 = km * 0.50 # menos de 200km, cobra 0.50 por km
cal2 = km * 0.45 # mais de 200km, cobra 0.45 por km
if km <= 200:
    print('{}Sua passagem entra na cota de R$ 0.50 por km{}'.format(cores['verde'], cores['fechamento']))
    print('{}Sua viagem é de {}KM e ficara no total de R$ {:.2f}{}'.format(cores['verde'], km, cal1, cores['fechamento']))
else:
    print('{}Sua passagem entra na cota de R$ 0.45 por km{}'.format(cores['verde'], cores['fechamento']))
    print('{}Sua viagem é de {}KM e ficara no total de R$ {:.2f}{}'.format(cores['verde'], km, cal2, cores['fechamento']))
print('{}Boa viagem!{}'.format(cores['vermelho'], cores['fechamento']))


# carlos daniel