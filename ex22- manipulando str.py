nome = str(input('Digite seu nome completo'))
print('Analisando seu nome...')
print('Seu nome em maiusculo: {}'.format(nome.upper())) # ira deixar o nome todo em maiusculo
print('Seu nome em minusculo: {}'.format(nome.lower())) # ira deixar o nome todo em minusculo
print(len(nome)-nome.count(" ")) # vai contar quantos caracter, no calo letras armazenados na var nome, tirando os espaços
print()

