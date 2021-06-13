class livros:
    variavel = 10
    def __init__(self, nome, autor, ano, editora):
        self.nome = nome
        self.autor = autor
        self.ano = ano
        self.editora = editora
    def adicionaPreco(self, preco):
        self.preco = preco
    def imprime(self):
        print('%s %s %d %s %d'%(self.nome, self.autor, self.ano, self.editora, self.preco))
livro1 = livros('Memórias Postumas de Bras Cubas','Machado de Assis',
                                               1890, 'Melhoramentos')
livro2 = livros('Capitães da Areia','Jorge Amado',1900, 'Melhoramentos')
livro1.adicionaPreco(100)
livro1.imprime()
livro1.adicionaPreco(200)
livro1.imprime()
print(type(livro1.ano))