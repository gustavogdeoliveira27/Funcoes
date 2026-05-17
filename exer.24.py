def progressiva(x):
    if x == 6:
        print("Finalizada")
    else:
        print(x)
        progressiva(x + 1)

progressiva(0)