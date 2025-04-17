#import math
"""Crie um algoritmo que leia um número e mostre o seu dobro, triplo e
a raiz quadrada"""

n = int(input('Digite um número: '))

#r = math.pow(n, 1/2)

print('O dobro de {} vale {}.\n'
      'O triplo de {} vale {}.\n'
      'A raiz quadrada de {} é igual a {:.2f}.'.format(n, (n*2), n, (n*3), n, (n**(1/2))))

"""Consegui realizar o exercício das duas formas, utilando o método pow()
e o cálculo dentro do .import, outra opção válida seria criar uma variável
para cada cálculo e usa-las prontas"""