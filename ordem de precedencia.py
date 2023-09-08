# ordem de precedencia 
# 1- é os parenteres ()
# 2 - é ** exponesiação 
# 3-  aqui vem *,/,//,% | desses quatros operadore, o que vai mandar que sera feito e quem vinher primeiro.
# 4 - e por ultimo vem, + (mais), -(menos)

# ex-01
num1,num2,num3 = 5,3,2
soma1 = num1+num2*num3  # nesse exemplo sera feito primerio a multipicação depois a soma
print(soma1)            # num2*num3 == 6, depois sera num1+5 == 11

# ex-02
n1,n2,n3,n4 = 3,5,4,2  # aqui ira ser feito primeiro a **, depois a multiplicação, e por fim a soma
soma2 =n1*n2+n3**n4    # n3**n4 == 16, depois n1**n2 == 15, depois a soma de 15+16 == 31
print(soma2)

# ex-03
n5,n6,n7,n8 = 3,5,4,2 # aqui será, primeiro o que esta dentre(),depois a ** , por fim a multiplicação
soma3 = n5*(n6+n7)**2 # (n6+n7) == 9, depois 9**2(9  ao quadrado) == 81, por fim 3*81 == 243
print(soma3)

# todos os exemplos, estou usando variaveis multiplas.abs]

# carlos daniel   24/08/2023