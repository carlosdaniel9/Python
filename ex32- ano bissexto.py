from datetime import date
print('Verificador de ano BISSEXTO')
ano = int(input('Digite o ano que você dejesa verificar, Digite 0 para verificar seu ano atual: '))
if ano == 0:
    ano = date.today().year # irar pegar somente o ano atual da sua maquina.
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:  # formulá para verificar se o ano é bissexto.
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} não é BISSEXTO'.format(ano))


# carlos daniel    29/09/2023