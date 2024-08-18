# Função que Exibe a Data e Hora Atual
def exibir_data_hora():
    from datetime import datetime
    agora = datetime.now()
    print(f"Data e hora atuais: {agora}")
    
 # Chamando a função
exibir_data_hora()