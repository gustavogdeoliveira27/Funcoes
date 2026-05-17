def regressiva(x):
    if x == 0:
        print("Contagem finalizada")
    else:
        print(x)
        regressiva(x - 1)

regressiva(5)
