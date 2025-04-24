"""Faça um programa que leia uma frase pelo teclado e mostre:
- Quantas vezes aparece a letra 'A'
- Em que posição ela aparece a primeira vez.
- Em que posição ela aparece pela última vez"""

frase = str(input('Digite uma frase: ')).strip().upper()



print('A letra A aparece {} vezes na frase.\n'
      'A primeira letra A apareceu na posição {}.\n'
      'A última letra A apareceu na posição {}.'.format(frase.count('A'), (frase.find('A') + 1), (frase.rfind('A') + 1)))