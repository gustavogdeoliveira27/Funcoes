def mostrar_dados(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

mostrar_dados(nome="Gustavo", Idade=20, cidade="Curitiba")