class Livro():
    def __init__(self):
        self.titulo = 'O monge e o executivo'
        self.isbn = 9988888
        print('Construtor criado')

    def imprime(self):
        print('Foi criado o livro {} e ISBN {}'.format(self.titulo, self.isbn))


Livro1 = Livro()
Livro1.imprime()