def processar_dados(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)

    soma = sum(args) if args else 0

    return  {
        "Número de args": len(args),
        "Soma dos args": soma,
        "Número de kwargs": len(kwargs),
        "Os kwargs são": kwargs
    }
resultado = processar_dados(1,2,3,4,5, nome="Gustavo", idade=20, cidade="Curitiba")
print(resultado)