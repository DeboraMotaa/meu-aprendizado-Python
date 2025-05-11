"""Escreva um programa em Python que leia um número inteiro
qualquer e peça para o usuário escolher qual será a base de
conversão: 1 para binário, 2 para octal e 3 para hexadecimal."""

num = int(input('Digite um número inteiro: '))
escolha = int(input('Escolha uma das bases de conversão: \n'
                    '[ 1 ] converter para BINÁRIO\n'
                    '[ 2 ] converter para OCTAL\n'
                    '[ 3 ] converter para HEXADECIMAL\n'
                    'Sua opção: '))

if escolha == 1:
    binario = bin(num)[2:]
    print('{} convertido para BINÁRIO é igual a {}.'.format(num, binario))
elif escolha == 2:
    octal = oct(num)[2:]
    print('{} convertido para OCTAL é igual a {}.'.format(num, octal))
elif escolha == 3:
    hexa = hex(num)[2:]
    print('{} convertido para HEXADECIMAL é igual a {}.'.format(num, hexa))
else:
    print('Opção inválida!')