r1 = float(input('Primeiro segmento'))
r2 = float(input('Segundo segmento'))
r3 = float(input('Terceiro segmento'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR triâgulo')
    # nesse caso como ja estou comparando se r1 é igual a r2, e se r2 é igual a r3, não precisa testar de r1 é igual a r3.
    # pois se o r1 e r2 são igual, e eu estou comparando o r2 que é igual o r1, com  o r3, eles são iguais.
    if r1 == r2 and r2 == r3: # se r1 for igual a r2 e r2 for igual a r3
        print('Equilatero')
    elif r1 != r2 and r2 != r3 and r3 != r1: # se r1 for diferente de r2 e r2 diferente de r3 e r3 diferente de r1
        print('Escaleno')
    else:
        print('Isósceles' )
else:
    print('Os degmentos acima NÃO PODEM FORMAR UM triângulo')




# carlos daniel    13/10/2023