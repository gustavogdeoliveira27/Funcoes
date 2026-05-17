def executar(funcao, valor):
    return funcao(valor)

def triplo(x):
    return x * 3

print(executar(triplo, 5))