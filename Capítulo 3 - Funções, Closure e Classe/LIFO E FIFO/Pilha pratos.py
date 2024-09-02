pilha_pratos = []

def adicionar_prato(prato):
  pilha_pratos.append(prato)
  print(f"Prato Adicionado {prato}")

def retirar_prato():
  if pilha_pratos:
    prato = pilha_pratos.pop()
    print(f"Prato foi Removido {prato}")
    return prato
  else:
    print("Não há mais pratos na Pilha!")
    return None
  

adicionar_prato("Prato 1")
adicionar_prato("Prato 2")
adicionar_prato("Prato 3")
adicionar_prato("Prato 4")


retirar_prato()
retirar_prato()
retirar_prato()
retirar_prato()
retirar_prato()