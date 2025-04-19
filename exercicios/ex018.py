"""Faça um programa qualquer que leia um ângulo qualquer e mostre na tela o valor
do seno, cosseno e tangente desse ângulo"""

from math import cos, sin, tan, radians

angulo = float(input('Digite o ângulo que você deseja: '))

seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print('O ângulo de {:.2f} tem o SENO de {:.2f}\n'
      'O ângulo de {:.2f} tem o COSSENO de {:.2f}\n'
      'O ângulo de {:.2f} tem a TANGENTE de {:.2f}'.format(angulo, seno, angulo, cosseno, angulo, tangente))