#string = input("Digite uma string: ")
string = "Socorram-me subi no onibus em Marrocos"
stringInvertida = ""

for indice in range(len(string) - 1, -1, -1):
    stringInvertida = stringInvertida + string[indice]

print(stringInvertida)