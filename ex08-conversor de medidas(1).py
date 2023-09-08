# Anotações gerais
# cada metro é equivalente a 100 centimetros 
# cada metro é equivalente a 1.000 milimetros 

medida = float(input('digite uma medida em metros'))
cm = medida * 100   # pegando o valor de medida e multiplicando por 100
mm = medida * 1000  # pegando o valor de medida e multiplicando por 1000

print('A medida em metros é {} \n Em centimetros é {} \n Em milimetros é {}'.format(medida, cm, mm))
# printado o valores, o \n serve para da quebra de linha.+