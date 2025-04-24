"""Crie um programa que leia o nome completo de uma pessoa e mostre:
O nome com todas as letras maiúsculas e minúsculas.
Quantas letras ao todoo (sem considerar espaços).
Quantas letras tem o primeiro nome."""

nome = str(input('Digite seu nome completo: ')).strip()

#Transformando em lista para pegar o index 0(o primeiro nome) e contar quantos caracteres tem
lista = nome.split()

print('Analisando seu nome...\n'
      'Seu nome em maiúsculas é {}\n'
      'Seu nome em minúsculas é {}\n'
      'Seu nome tem ao todo {} letras\n'
      'Seu primeiro nome é {} e ele tem {} letras'.format(nome.upper(), nome.lower(), len(nome) - nome.count(' '), lista[0], len(lista[0])))