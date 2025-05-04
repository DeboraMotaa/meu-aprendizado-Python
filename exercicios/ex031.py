"""Desenvolva um programa que pergunte a distância de uma viagem em
Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens
de até 200Km e R$0,45 parta viagens mais longas."""

km = float(input('Qual a distância da viagem em Km? '))

print('Você está prestes a começar uma viagem de {:.1f} Km.'.format(km))
if km <= 200:
    passagem = km * 0.50
else:
    passagem = km * 0.45

print('E o preço da sua passagem será de R${:.2f}'.format(passagem))