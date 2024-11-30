class Livro:
    def __init__(self, titulo, autor, isbn, quantidade):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.quantidade = quantidade

    def exibir_detalhes(self):
        print(f"Título: {self.titulo}, Autor: {self.autor}, ISBN: {self.isbn}, Quantidade: {self.quantidade}")

    def verificar_disponibilidade(self):
        return self.quantidade > 0