# modelo 1 | mostrando a porcentagem 
bolsa = 100
porcente = bolsa * 20 / 100  # nesse codido so irar  mostra quanto é 10% de 100, que no caso é 10
print(porcente)

# modelo 2 | diminiundo a porcentagem de 10%  com a variavel calça, que ira da 180
calça = 200
desc = calça - (calça * 10 / 100) # o codigo (calça * )
print(desc)

# modelo 3 | exemplo com soma e menos, seu valor de porcentagem, definido entre parenteres, que da preferençia 
# para fazer logo o calculo da porcentagem, e a variavel mais o sinal de + ira soma com o resultado do calculo, feito antes da %
tenis = 300
desconto = tenis - (tenis * 5 / 100) # tirando 5% de 300, o valor esta sendo diminuido com os propio 300
acressio = tenis + (tenis * 8 / 100) # aumentando 8% de 300, o valor esta sendo somado com os propio 300

print('você pagando avista, o tênis de R${}, ira sair por R${}'.format(tenis, desconto))
print('pagando a prazo o tênis de R${}, com aumento de 8%, irar sair por R${}'.format(tenis, acressio))