num1 = 160
num2 = 20

soma = num1 + num2
subtracao = num1 - num2
divisao = num1 / num2
multiplicacao = num1 * num2

def calculadora(num1, num2 , operacao):
  if operacao == "soma":
     return "num1 + num2"
  elif operacao == "subtracao":
    return num1 - num2
  elif operacao == "multiplicacao":
    return num1 * num2
  elif operacao == "divisao":
    return num1 / num2 if num2 !=0 else "erro"
print(f"O resultado da soma é: {soma}")
