from collections import deque

# Inicializa as filas de clientes
fila_prioritaria = deque()
fila_comum = deque()

def add_cliente(nome, idade):
    if idade >= 60:
        fila_prioritaria.append((nome, idade))
    else:
        fila_comum.append((nome, idade))
    print(f"O cliente {nome}, com {idade} anos, entrou na fila.")

def atender_cliente():
    if fila_prioritaria:
        cliente_atendido = fila_prioritaria.popleft()
        print(f"O cliente {cliente_atendido[0]} (idade {cliente_atendido[1]}) foi atendido.")
    elif fila_comum:
        cliente_atendido = fila_comum.popleft()
        print(f"O cliente {cliente_atendido[0]} (idade {cliente_atendido[1]}) foi atendido.")
    else:
        print("Não há clientes na fila.")

def main():
    while True:
        acao = input("Digite 'add' para adicionar um cliente ou 'at' para atender um cliente (ou  'sair q' para encerrar): ").strip().lower()

        if acao == 'add':
            nome = input("Digite o nome do cliente: ").strip()
            idade = int(input("Digite a idade do cliente: ").strip())
            add_cliente(nome, idade)

        elif acao == 'at':
            atender_cliente()

        elif acao == 'q':
            print("Encerrando o programa.")
            break
        else:
            print("Comando não reconhecido. Por favor, digite 'adicionar', 'atender' ou 'sair'.")


if __name__ == "__main__":
    main()