class pessoa:
    def __init__(self, nome, id, end): # construtor da class e seu atributos
        self.nome = nome
        self.id = id 
        self.end = end
    
    def saida(self): # metodo da class | nesse caso esta usando o metodo para retornar o propios 
        return self.nome, self.id, self.end
    
pessoa1 = pessoa ('carlos', '123', 'rua A') # variavel 

print('Olá {}, seu id é {}, mora na {}'.format(pessoa1.nome, pessoa1.id, pessoa1.end))