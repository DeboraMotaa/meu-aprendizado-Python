"""Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele."""

algo = input('Digite algo: ')

"""
print('O tipo primitivo desse valor é', type(algo))
print('Só tem espaços?', algo.isspace())
print('É numérico?', algo.isnumeric())
print('É alfabético?', algo.isalpha())
print('É alfanumérico?', algo.isalnum())
print('Está em letras maiúsculas?', algo.isupper())
print('Está em letras minúsculas?', algo.islower())
print('Está captalizada?', algo.istitle())
"""

"""A segunda parte é reproduzir o exercício utilixando o método .format"""
print('O tipo primitivo desse valor é {}!\nSó tem espaços? {}!\nÉ numérico? {}!\nÉ alfabético? {}!\nÉ alfanumérico? {}!\nEstá em letras maiúsculas? {}!\nEstá em letras minúsculas? {}!\nEstá captalizada? {}!'.format(type(algo), algo.isspace(), algo.isnumeric(), algo.isalpha(), algo.isalnum(), algo.isupper(), algo.islower(), algo.istitle()))
