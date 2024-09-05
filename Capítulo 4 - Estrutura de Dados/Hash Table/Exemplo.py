class TabelaHash:
  def __init__(self, size):
    self.size = size
    self.table = [None]*size

  def hash_function(self, key):
    return sum(ord(char) for char in key) % self.size

  def inserir(self, key, valor) :
    indice = self.hash_function(key)
    if self.table[indice] is None:
      self.table[indice] = [(key, valor)]
    else:
      self.table[indice].append((key, valor))

  def busca(self, key):
    indice = self.hash_function(key)
    if self.table[indice] is not None:
      for sk in self.table[indice]:
        if sk[0] == key:
          return sk[1]

    return None
  
Tabela = TabelaHash(10)

Tabela.inserir("Maria", 12345)
Tabela.inserir("Joaquim", 56789)
Tabela.inserir("Diego", 74125)
Tabela.inserir("Luiz", 84359)

print(Tabela.busca("Luiz"))





