# Exemplo de uso de estruturas condicionais em Python

resposta = input('Você vai estudar hoje? ').lower()

if resposta == 'sim':
    print('Parabéns, continue assim!')
elif resposta == 'não':
    print('Tente organizar um tempo para estudar.')
else:
    print('Resposta inválida.')
