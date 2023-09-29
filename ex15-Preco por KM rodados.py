dias = float(input('Quantos dias você ficou com o carro?'))
km = float(input('Quantos KM você rodou?'))

valor_dia = 60  # valor por dia do aluguel do carro 
valor_km = 0.15 # valor por km rodado 
resultado = (dias * valor_dia) + km * valor_km
# a variavel acima está, primeio o do parentre que é multiplicando a var dias por valor_dia que é 60
# em seguida ele multiplica kM por valor_km, por final soma o resultado das duas multiplicação
# lembrando que a multiplicação sempre vem antes,e como tinha duas nesse exercicio, coloquie a primeira do dias entre parentes, para ser feita primeiro
# ai so depois a soma, pois ela é a ultima na ordem de orecedencia
print('Você ficou {} dias, com o carro e rodou {} KM, que da R${:.2f} no total'.format(dias, km, resultado))


# carlos daniel   31/08/2023