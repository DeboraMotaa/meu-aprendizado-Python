"""Faça um programa que leia o ano de nascimento de um jovem e
informe, de acordo com a sua idade, se ele ainda vai se alistar
ao serviço militar, se é a hora exata de se alistar ou se já passou
do tempo do alistamento. Seu programa também deverá mostrar o tempo
que falta ou que passou do prazo."""

from datetime import date

ano_nasc = int(input('Digite seu ano de nascimento: '))

ano_atual = date.today().year
idade = ano_atual - ano_nasc

print('Quem nasceu em {} tem {} anos em {}.'.format(ano_nasc, idade, ano_atual))

if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o alistamento.'.format(saldo))
    ano = ano_atual + saldo
    print('Seu alistamento será em {}.'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Seu alistamento foi há {}.'.format(saldo))
    ano = ano_atual - saldo
    print('Seu alistamento foi em {}.'.format(ano))
    