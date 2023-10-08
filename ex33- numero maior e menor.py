n1 = int(input('Numero 1: '))
n2 = int(input('Numero 2: '))
n3 = int(input('Numero 3: '))
# vai verificar o número menor.
menor = n1 # aqui estou supondo que o menor é n1, em seguida faço o teste em relação aos outros.
if  n2 < n1 and n2 < n3:
    menor= n2
if n3 < n1 and n3 < n2:
    menor = n3
print('O número menor é {}'.format(menor))
# vai verificar o número maior.
maior = n1  # aqui estou supondo que o maior é n1, em seguida faço o teste em relação aos outros.
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('O número maior é {}'.format(maior))


# carlos daniel    29/09/2023