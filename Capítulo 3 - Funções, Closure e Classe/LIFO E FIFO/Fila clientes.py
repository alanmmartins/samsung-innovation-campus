from collections import deque
fila_cliente = deque

# Inicializa a fila de clientes como uma instância de deque
fila_cliente = deque()

def add_cliente(nome):
    fila_cliente.append(nome)  # Adiciona o nome do cliente à fila
    print(f"O cliente {nome} entrou na fila.")

def atender_cliente():
    if fila_cliente:
        cliente_atendido = fila_cliente.popleft()
        print(f"O cliente {cliente_atendido} foi atendido.")
    else:
        print("Não há clientes na fila.")

# Adiciona clientes à fila
add_cliente("alaa")
add_cliente("alae")
add_cliente("alai")
add_cliente("alao")
add_cliente("alau")


atender_cliente()
atender_cliente()
atender_cliente()
atender_cliente()
atender_cliente()
atender_cliente()