print('-=-' *20)
print('Analisador de triângulo')
print('-=-' *20)
r1 = float(input('Primeiro seguimento: '))
r2 = float(input('Segundo seguimento: '))
r3 = float(input('Terceiro seguimento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2: # formula para verificar se os números digitados, podem forma um triângulo.
    print('Os seguimentos acima, podem forma um triângulo')
else:
    print('Os seguimentos acima, não podem forma um triângulo')



# carlos daniel    29/09/2023