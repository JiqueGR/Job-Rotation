valor = int(input("Digite um número: "))

num1, num2 = 0, 1
aux = 0

while num1 <= valor:
    if num1 == valor:
        print("O valor", valor, "pertence à sequência de Fibonacci.")
        break
    aux = num1
    num1 = num2
    num2 = aux + num2

else:
    print("O valor", valor, "nao pertence à sequência de Fibonacci.")