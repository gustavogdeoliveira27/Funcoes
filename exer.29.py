def calculadora(a, b, operacao):
    if operacao == "+":
        return a + b
    elif operacao == "-":
        return a - b
    elif operacao == "*":
        return a * b
    elif operacao == "/":
        if b == 0:
            return "Erro: divisão por 0"
        return a / b
    elif operacao == "%":
        return a % b
    else:
        return "Operação inválida"
    
print(calculadora(4, 2, "+"))
print(calculadora(4, 2, "-"))
print(calculadora(4, 2, "*"))
print(calculadora(4, 2, "/"))
print(calculadora(4, 2, "%"))
    