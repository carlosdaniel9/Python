nome = str(input('Digite seu nome completo: '))
print('Analisando seu nome...')
print('Seu nome em maiusculo: {}'.format(nome.upper())) # ira deixar o nome todo em maiusculo
print('Seu nome em minusculo: {}'.format(nome.lower())) # ira deixar o nome todo em minusculo
print('{} seu nome tem {} letras'.format(nome, len(nome)-nome.count(" "))) # vai contar quantos caracter, no calo letras armazenados na var nome, tirando os espaços
# pegango o primeiro nome do usúario
# método 1
print('- Método 1 usando o find, para encontrar o primeiro espaço')
print('Seu primeiro nome tem {} letras'.format(nome.find(' '))) # ira indentificar o primeiro espaço, começando do 0, que será o primeiro nome do usuario


# método 2
print('- Método 2, usando uma var com split, depois pega o nome 0 d lista, que será o primeiro nome.')
separa = nome.split()
print('seu primeiro nome é {} e tem {} letras'.format(separa[0], len(separa[0])))



# Carlos     22/09/2023