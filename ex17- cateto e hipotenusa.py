import math
co = float(input('Qual a medida do cateto oposto?'))
ca = float(input('Qual a medida do cateto adjacente?'))

cal = (co ** 2 + ca ** 2) ** (1/2) # essa é a formula matematica 
cal2 = math.hypot(co, ca)

print('A soma entre o cateto oposto pelo adjacente, da uma hipotenusa de {:.2f}'.format(cal))
print('a hipotenusa de cateto oposto {} e do adjacente {} é {:.2f}, usando hypot do math'.format(co, ca, cal2))


# carlos daniel  9/09/2023