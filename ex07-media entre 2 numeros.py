n1 = float(input('Caro aluno, digite sua primeira nota'))
n2 = float(input('segunda nota'))
media = (n1 + n2) / 2 # aqui esta somando os valores da variavel, de dividindo por 2 
# os () para n1+n2, para para primeiro fazer a soma das notas, ai so depois ele dividir por 2ß

print('A média entre {:.1f}, e {:.1f} é {:.1f}'.format(n1, n2, media))
# :.1f, está dizendo que depopis do ponto flutuante, coloque apenas 1 digite(casa decimas)