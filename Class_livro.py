class livro:
    def __init__(self,id_livro, titulo, ano, autor):
        self.id_livro = id_livro
        self.titulo = titulo
        self.ano = ano
        self.autor = autor
        
    def mostrar(self):
	    print("ID livro: {} Tilulo: {} Ano: {} Autor: {}".format(str(self.id_livro),self.titulo,str(self.ano),self.autor))