nome = str(input('Digite seu nome completo: ')).strip()

nomes = nome.split()
pnome = nomes[0]
unome = nomes[-1]

print('Muito prazer em te conhecer!\n'
      'Seu primeiro nome é {}\n'
      'Seu último nome é {}'.format(pnome, unome))