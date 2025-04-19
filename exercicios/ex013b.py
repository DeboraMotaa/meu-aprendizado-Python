"""Crie um algoritmo que leia o valor do produto e mostre os seus respectivos
valores no pix (com desconto) e no cartão de crédito (com juros)."""

valor = float(input('Qual o valor do produto? R$ '))

pix = valor - (valor * 5 / 100)
credito = valor + (valor * 5 / 100)

print('O produto no valor de R${:.2f} no pix, com desconto de 5%, passa a ser R${:.2f}!\n'
         'No cartão de crédito, com juros de 5%, passa a sar R${:.2f}!'.format(valor, pix, credito))