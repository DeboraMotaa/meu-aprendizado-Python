"""Escreva um programa que converta uma temperatura digitada em ºC para ºF"""

c = float(input('Informe a temperatura em ºC: '))

f = c * 1.8 + 32

print('A temperatura de {:.1f}ºC corresponde a {:.1f}ºF!'.format(c, f))