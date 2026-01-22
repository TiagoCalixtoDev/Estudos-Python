# Cálculo simples de IMC

nome = input('Digite seu nome: ')
altura = float(input('Digite sua altura (ex: 1.75): '))
peso = float(input('Digite seu peso (kg): '))

imc = peso / (altura ** 2)

print(f'{nome} tem {altura}m de altura, pesa {peso}kg e seu IMC é {imc:.2f}')
