class Livro:
    def __init__(self,titulo, autor, edicao,qtd_pagina):
        self.titulo = titulo
        self.autor = autor
        self.edicao = edicao
        self.qtd_pagina = qtd_pagina
    
    def __str__(self):
        return (f'titulo {self.titulo} - autor {self.autor} - edicao - {self.edicao} - paginas {self.qtd_pagina}')
    

livro1 = Livro('Fundamento de Python','Fulano de Tal','2022','215')
livro2 = Livro('Logica de Programação','Jose Nacimento','2017','197')
livro3 = Livro('Guia Definitivo Python','ABC','2015','607')
livro4 = Livro('Logica de Programação 2','Bill','2020','155')

# print(livro1)
# print(livro2)
# print(livro3)
# print(livro4)
# print(livro2.get_detalhes())


# Criem 4 instancias de Livro

# Criem uma classe produtos que tenha 5 atributos e três metodos: um para pega o preço e outro para atualizar o preço e o str que traga a descrição completa

class Produto:
    def __init__(self,nome,preco,marca,quantidade,tamanho):
        self.nome = nome
        self.preco = preco
        self.marca = marca
        self.quantidade = quantidade
        self.tamanho = tamanho
    
    def get_preco(self):
        return self.preco
    
    def set_preco(self, novopreco):
        self.preco = novopreco
    
    def __str__(self):
        return (f'{self.marca} {self.nome} - {self.quantidade} x R$ {self.preco}') 
        

prod1 = Produto('S23',4499, 'Samsung', '1', "9'")
print(prod1.get_preco())
prod1.set_preco(999)
print(prod1.get_preco())
print(prod1)
