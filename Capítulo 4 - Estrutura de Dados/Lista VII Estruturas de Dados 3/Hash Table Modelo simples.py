class TabelaHash:
    def __init__(self, size):

        self.size = size
        self.table = [[] for _ in range(size)]  # Inicializa com listas vazias para lidar com colisões

    def hash_function(self, key):
        """
        Função de hash para converter a chave (ISBN) em um índice da tabela.
        :param key: O ISBN do livro.
        :return: Índice da tabela onde o livro deve ser armazenado.
        """
        return hash(key) % self.size

    def adicionar_livro(self, isbn, titulo, autor):
        """
        Adiciona um livro à tabela de hash.
        :param isbn: O ISBN do livro.
        :param titulo: O título do livro.
        :param autor: O autor do livro.
        """
        indice = self.hash_function(isbn)
        # Verifica se o ISBN já está na tabela e atualiza o livro se necessário
        for i, (k, v) in enumerate(self.table[indice]):
            if k == isbn:
                self.table[indice][i] = (isbn, (titulo, autor))
                return
        # Caso contrário, adiciona o novo livro
        self.table[indice].append((isbn, (titulo, autor)))

    def buscar_livro(self, isbn):
        """
        Busca um livro na tabela de hash pelo ISBN.
        :param isbn: O ISBN do livro.
        :return: Uma tupla contendo o título e o autor do livro, ou None se o livro não for encontrado.
        """
        indice = self.hash_function(isbn)
        for k, v in self.table[indice]:
            if k == isbn:
                return v
        return None

    def remover_livro(self, isbn):
        """
        Remove um livro da tabela de hash pelo ISBN.
        :param isbn: O ISBN do livro.
        """
        indice = self.hash_function(isbn)
        for i, (k, v) in enumerate(self.table[indice]):
            if k == isbn:
                del self.table[indice][i]
                return

# Exemplo de uso da classe TabelaHash
biblioteca = TabelaHash(10)

# Adicionando livros
biblioteca.adicionar_livro('1', 'O Senhor dos Anéis', 'J.R.R. Tolkien')
biblioteca.adicionar_livro('2', '1984', 'George Orwell')

# Buscando livros
print(biblioteca.buscar_livro('1'))  #
print(biblioteca.buscar_livro('2'))  #
print(biblioteca.buscar_livro('0'))  #

# Removendo um livro
biblioteca.remover_livro('5')
print(biblioteca.buscar_livro('5'))  #