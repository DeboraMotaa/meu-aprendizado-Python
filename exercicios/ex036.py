"""Escreva um programa para aprovar o empréstimo bancário para a
compra de uma casa. Pergunte o valor da casa, o salário do comprador e em
quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do
salário ou então o empréstimo será negado."""

valor_casa = float(input('Qual o valor da casa? R$ '))
salario_comprador = float(input('Qual o salário do comprador? R$ '))
anos = int(input('Em quantos anos irá pagar? '))
meses = anos * 12
parcela = valor_casa / meses

print('Para pagar a casa de R$ {:.2f} em {} anos a prestação será de R$ {:.2f}'.format(valor_casa, anos, parcela))

if parcela >  salario_comprador * 0.3:
      print('Empréstimo NEGADO!')
else:
      print('Empréstimo APROVADO!')