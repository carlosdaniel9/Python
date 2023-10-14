nota1 = float(input('Digite a nota de sua primeira prova: '))
nota2 = float(input('Digite a nota de sua segunda prova: '))
media = (nota1 + nota2) / 2
#print('Tirando {:.1f} e {:.1f} sua média é {:.1f}'.format(nota1, nota2, media))
if media < 5:
    print('Você com {:.1f} está reprovado'.format(media))
elif media <= 6.9:
    print('Com {:.1f} cocê está de recuperação'.format(media))
else: 
    print('Parabéns você foi aprovado com {:.1f}'.format(media))




# carlos daniel    12/10/2023