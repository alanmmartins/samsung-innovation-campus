class TabelaHash:
    def __init__(self, size):
        """
        Inicializa a tabela de hash com um tamanho específico.
        :param size: O tamanho da tabela de hash.
        """
        self.size = size  # Define o tamanho da tabela de hash
        # Inicializa a tabela com listas vazias para lidar com colisões
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        """
        Função de hash para converter a chave (ISBN) em um índice da tabela.
        :param key: O ISBN do livro.
        :return: Índice da tabela onde o livro deve ser armazenado.
        """
        # Calcula o índice usando a função hash e o operador módulo para garantir que esteja dentro dos limites
        return hash(key) % self.size

    def adicionar_livro(self, isbn, titulo, autor):
        """
        Adiciona um livro à tabela de hash.
        :param isbn: O ISBN do livro.
        :param titulo: O título do livro.
        :param autor: O autor do livro.
        """
        indice = self.hash_function(isbn)  # Calcula o índice para o ISBN
        # Verifica se o ISBN já está na tabela e atualiza o livro se necessário
        for i, (k, v) in enumerate(self.table[indice]):
            if k == isbn:
                self.table[indice][i] = (isbn, (titulo, autor))
                return
        # Se não encontrou, adiciona o novo livro na lista do índice
        self.table[indice].append((isbn, (titulo, autor)))

    def buscar_livro(self, isbn):
        """
        Busca um livro na tabela de hash pelo ISBN.
        :param isbn: O ISBN do livro.
        :return: Uma tupla contendo o título e o autor do livro, ou None se o livro não for encontrado.
        """
        indice = self.hash_function(isbn)  # Calcula o índice para o ISBN
        # Percorre a lista de pares chave-valor no índice calculado
        for k, v in self.table[indice]:
            if k == isbn:
                return v  # Retorna o título e o autor do livro
        return None  # Retorna None se o livro não for encontrado

    def remover_livro(self, isbn):
        """
        Remove um livro da tabela de hash pelo ISBN.
        :param isbn: O ISBN do livro.
        """
        indice = self.hash_function(isbn)  # Calcula o índice para o ISBN
        # Percorre a lista de pares chave-valor no índice calculado
        for i, (k, v) in enumerate(self.table[indice]):
            if k == isbn:
                del self.table[indice][i]  # Remove o livro da lista
                return

def menu():
    """
    Exibe o menu e gerencia as operações de adicionar, buscar e remover livros.
    """
    biblioteca = TabelaHash(10)  # Cria uma instância da tabela de hash com tamanho 10

    while True:
        # Exibe o menu de opções
        print("\nSistema de Cadastro de Livros")
        print("1. Adicionar Livro")
        print("2. Buscar Livro")
        print("3. Remover Livro")
        print("4. Sair")
        opcao = input("Escolha uma opção (1/2/3/4): ")  # Captura a opção do usuário

        if opcao == '1':
            # Adiciona um livro
            isbn = input("Digite o ISBN do livro: ")
            titulo = input("Digite o título do livro: ")
            autor = input("Digite o nome do autor: ")
            biblioteca.adicionar_livro(isbn, titulo, autor)  # Adiciona o livro à tabela
            print("Livro adicionado com sucesso!")

        elif opcao == '2':
            # Busca um livro
            isbn = input("Digite o ISBN do livro para buscar: ")
            resultado = biblioteca.buscar_livro(isbn)  # Busca o livro na tabela
            if resultado:
                # Se o livro for encontrado, exibe o título e o autor
                print(f"Título: {resultado[0]}, Autor: {resultado[1]}")
            else:
                print("Livro não encontrado!")

        elif opcao == '3':
            # Remove um livro
            isbn = input("Digite o ISBN do livro para remover: ")
            biblioteca.remover_livro(isbn)  # Remove o livro da tabela
            print("Livro removido com sucesso!")

        elif opcao == '4':
            # Sair do sistema
            print("Saindo do sistema...")
            break  # Sai do loop e encerra o programa

        else:
            # Opção inválida
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    menu()  # Chama a função menu para iniciar o sistema