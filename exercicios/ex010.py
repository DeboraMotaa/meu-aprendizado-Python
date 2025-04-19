"""Crie um programa que mostre quanto dinheiro uma pessoa tem na carteira e
mostre quantos Dólares ela pode comprar.
Considere US$1,00 = R$3,27"""

r = float(input('Quanto dinheiro você tem na carteira em reais? R$ '))

d = r / 3.27

print('Com R$ {:.2f} vocÊ pode comprar US$ {:.2f}!'.format(r, d))