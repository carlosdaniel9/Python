from datetime import date
anoAtual = date.today().year #  está pegando data atual da máquina.
nascimento = int(input('Em que ano você nasceu? '))
idade = anoAtual - nascimento  # vai verfificar qunatos anos o usuario tem.
print('Quem nasceu em {} tem {} anos em {}'.format(nascimento, idade, anoAtual))
if idade == 18:
    print('Você tem que se alistar imediatamente.')
elif idade < 18:
    saldo = 18 -idade # está pegando 18 menos a idade, que vai da qunatos falta pra ele se alisatar.
    print('Ainda falta {} anos para seu alistamento'.format(saldo))
    ano = anoAtual + saldo # A variavel saldo mostra quantos ano falta, e soma o saldo + anoAtual , vai da o ano que vai ser o alistamento.
    print('Seu alistamento será em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18 # pega a idade e diminui 18, para ver quantos anos passou do alistamento.
    print('Você ja deveria ter se alistado a {} anos'.format(saldo))
    ano = anoAtual - saldo # Essa variavel pega o anoatual menos o saldo, que vai da o que foi o alistamento.
    print('Seu ano de alistamento foi em {}'.format(ano))





# carlos daniel     10/10/2023