from datetime import date
anoAtual = date.today().year
nascimento = int(input('Em qual ano você nasceu?'))
idade = anoAtual - nascimento

if idade <= 9:
    print('Com {} anos você é um nadador MIRIM'.format(idade))
elif idade <= 14:
    print('Com {} anos você é um nadador INFANTIL'.format(idade))
elif idade <= 19:
    print('Com {} anos você é um nadador JÚNIOR'.format(idade))
elif idade <= 25:
    print('Com {} anos você é um nadador SÊNIOR'.format(idade))
else:
    print('Com {} anos você é um nadador MASTER'.format(idade))



# carlos daniel    13/10/2023