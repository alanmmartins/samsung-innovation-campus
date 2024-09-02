texto_pilha = []

def escrever_texto(texto, novo_texto):
  texto_pilha.append(texto)
  return texto + novo_texto

def desfazer():
  if texto_pilha:
    return texto_pilha.pop()

  return ""
texto = ""
texto = escrever_texto(texto, "Olá, ")
print(f"Texto atual: {texto}")

texto = escrever_texto(texto, "Mundo! ")
print(f"Texto atual: {texto}")

texto = desfazer()
print(f"Texto após usar a função Desfazer: {texto}")
