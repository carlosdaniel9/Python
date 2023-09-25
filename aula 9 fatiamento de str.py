# Fatiamento de str

nome = 'carlos daniel'
print(nome[0])   # ira pegar o c
print(nome[0:7])   # ira nome carlos | o número final, sempre pega 1 antes, como aqui ta o 7, ira aparecer do 0 a 6
print(nome[:7])  # se não colocar o primeiro número, ira iniciar no 0 e para no 7, nese exemplo.
print(nome[7:])  # inicia no 7 e so irar para nofinal, pois não tem nenhum número definido para encerrar esse fatamemnto
print(nome[0:13:2])   # o :2 depois do 13, siguinifica que, entre o 0 e 13, ele vai pular de 2 em 2. na linha abaixo está usando o 3
print(nome[0::3]) # inicia no 0, como não tem o outro numero após o primmeiro :, siginifica que vai até o fonal, pulando de 3 em 3

# análise

print(len(nome)) # o len vai mostra o comprimento.
print(nome.count('a')) # o count é de contar, vai mostra quantas vezes vai aparecer o a, minúsculo, se estivesse um maiusculo, não iria aparcer na contagem.
print(nome.count('a', 0,7))  # vai contar, quantas vezes vai aparecer o a, do 0 a caracter 7
print(nome.find('car')) # vai ver onde começa o car, no caso será no caracter 0
print(nome.find('hello')) # vai retornar -1, que significa que não tem hello na var nome

print('hello' in nome) # usando o in, vai verificar se tem o nome hello na var nome, nesse caso vai retornar False



