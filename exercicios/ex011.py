""" Faça um programa que leia a largura e a altura de uma parede em metros,
calcule a sua área e a quantidade de tinta necessária para pinta-la, sabendo
que cada litro de tinta, pinta uma área de 2m²"""

l = float(input('Largura da parede: '))
a = float(input('Altura da parede: '))

area = l * a
tinta = area / 2

print('Sua parede tem a dimensão de {:.2f}x{:.2f} e sua área é de {:.2f}m².\n'
      'Para pintar essa parede, você precisará de {:.2f}l de tinta.'.format(l, a, area, tinta))