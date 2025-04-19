"""Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com aumento de 15%"""

s = float(input('Qual é o salário do funcionário? R$ '))

ns = s + (s * 15 / 100)

print('O funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}!'.format(s, ns))