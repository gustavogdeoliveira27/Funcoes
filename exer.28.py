lista = [1,2,3,4,5,6,7,8]

def media(lista):
    """"
    Calcula a média dos valores de uma lista.

    Parâmetros:
    lista(list): Lista de números (int ou float)

    Retorno:
    float: A média dos valores da lista.

    Levanta:
    ValueError: Se a lista estiver vazia.
    """
    if len(lista) == 0:
        raise ValueError("A lista não pode estar vazia")
    
    return sum(lista) / len(lista)

help(media)
