nome = str(input('Digite seu nome completo: ')).strip() # strip tira os espaços
n = nome.split() # separa os nome 
print('seu nome completo é {}'.format(nome))
print('O primeiro nome é {}'.format(n[0])) # vai pegar o primeiro nome, ja separado pela var n 
print('Seu ultimo nome é {}'.format(n[len(n)-1])) # vai pegar o ultimo nome, ja separado pela var n 


# carlos daniel    26/09/2023