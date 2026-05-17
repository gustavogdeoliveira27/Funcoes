def saudacao(nome, periodo="noite", mensagem="bem"):
    print(f"Boa {periodo} {nome}, tudo {mensagem}?")

saudacao("Gustavo")


def saudacao(nome, periodo, mensagem):
    print(f"Bom {periodo} {nome}, tudo {mensagem}?")

saudacao("Gustavo", "dia", "certo")