# 🧠 Semana 3: Estruturas Condicionais em Python

Durante essa semana, aprendi sobre **condições simples, compostas e simplificadas**.  
Essas estruturas são fundamentais para que o programa tome decisões com base em determinadas situações.

## Condições em Python 🐍

### 🔹 Condição Simples

Usa apenas o `if` para avaliar uma situação.

```python
if carro.esquerda():
    print('Vire à esquerda')
```
### 🔹 Condição Composta
Utiliza if e else, permitindo dois caminhos diferentes.

```
if carro.esquerda():
    print('Vire à esquerda')
else:
    print('Vire à direita')
  ```
### 🔹 Condição Simplificada
Uma forma reduzida de escrever uma estrutura condicional:

```
tempo = int(input('Quantos anos tem seu carro?'))
print('Carro novo') if tempo <= 3 else print('Carro velho')
print('--FIM--')
```

### 🔹 Forma tradicional equivalente:

```
tempo = int(input('Quantos anos tem seu carro?'))
if tempo <= 3:
    print('Carro novo')
else:
    print('Carro velho')
print('--FIM--')
```

### ✨ Conclusão
Com esse conteúdo, entendi que a forma como estruturamos as condições no código pode variar, mas o importante é que elas sempre nos ajudam a guiar o fluxo da execução. 🚦💡
