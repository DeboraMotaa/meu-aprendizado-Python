"""
Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor
"""
num = int(input('Digite um número: '))

ant = num - 1
suc = num + 1

print('O número escolhido foi {}. O número antecessor a ele é {} e o sucessor é {}.'. format(num, ant, suc))

"""
Outra forma de executar é: .format(num, (num-1), (num+1))
Teria o mesmo resultado e quando não usamos variáveis economizamos memória então,
em alguns casos, pode ser a melhor opção.
"""