"""Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela
a sua porção inteira

Ex: Digite um número: 6.127
O número 6.127 tem a parte inteira 6"""

from math import trunc

valor = float(input('Digite um valor: '))
resultado = trunc(valor)

print('O valor digitado foi {} e a sua porção inteira é {}.'.format(valor, resultado))