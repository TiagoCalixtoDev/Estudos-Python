entrada = input("Digite um número inteiro: ")

try:
    numero = int(entrada)

    if numero % 2 == 0:
        print("O número é par")
    else:
        print("O número é ímpar")

except ValueError:
    print("Você não digitou um número inteiro")
