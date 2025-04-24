# 📚 Resumo Semanal - Aprendizados em Python

## Semana de Estudos: Módulos e Manipulação de Texto 🐍

---

### 🧩 Módulos em Python

O Python vem com um núcleo "cru", ou seja, com o essencial para rodar programas simples. Para funcionalidades adicionais, usamos **módulos**, que funcionam como **bibliotecas**. Eles precisam ser **importados** antes do uso:

```python
import doce  # importa toda a biblioteca
from doce import chocolate  # importa um item específico
```

### 📐 Biblioteca `math`

Módulo nativo que traz funções matemáticas:

- `ceil`: arredonda para cima
- `floor`: arredonda para baixo
- `trunc`: elimina a parte decimal
- `pow`: potência (igual a `**`)
- `sqrt`: raiz quadrada
- `factorial`: fatorial
- `hypot`: hipotenusa
- `sin`, `cos`, `tan`: trigonometria
- `radians`: converte para radianos

Exemplo com a biblioteca completa:
```python
import math
raiz = math.sqrt(25)
```

Importando só o necessário:
```python
from math import sqrt
raiz = sqrt(25)
```

Importando múltiplos recursos:
```python
from math import sqrt, pow
```

### 🎲 Módulo `random`

Usado para gerar aleatoriedade:

**Escolher aleatoriamente um item de uma lista:**
```python
import random
escolhido = random.choice(['maçã', 'banana', 'uva'])
```

**Embaralhar uma lista:**
```python
random.shuffle(lista)
```

### 🎶 Módulo `pygame`

Para carregar músicas, imagens e vídeos:
```python
import pygame
pygame.init()
pygame.mixer.music.load('nomeDoArquivo.mp3')
pygame.mixer.music.play()
input(pygame.event.wait())
```

### 📦 Como explorar bibliotecas Python

1. Acesse [python.org](https://www.python.org)
2. Vá em "Docs"
3. Escolha sua versão
4. Clique em "Library Reference"

---

## 📝 Manipulação de Texto (Strings)

### Atribuição
```python
frase = 'Curso em Vídeo Python'
```
Cada caractere ocupa um índice na memória (de 0 a 20).

### Fatiamento
```python
frase[9]        # 'V'
frase[9:13]     # 'Víde'
frase[9:21]     # 'Vídeo Python'
frase[9:21:2]   # 'VdpPto'
frase[:5]       # 'Curso'
frase[15:]      # 'Python'
frase[9::3]     # 'VePh'
```

### Análise
```python
len(frase)                # comprimento da string
frase.count('o')          # quantos "o" existem
frase.count('o', 0, 13)   # conta "o" entre os índices 0 e 12
frase.find('deo')         # retorna índice de início de 'deo'
'Curso' in frase          # verifica existência da palavra
frase.rfind('a')          # última posição do caractere
```

### Transformação
```python
frase.replace('Python', 'Android')   # troca a palavra Python por Andoid
frase.upper()                        # deixa em maiúsculo
frase.lower()                        # deixa em minúsculo
frase.capitalize()                   # deixa a primeira letra da string maiúscula
frase.title()                        # deixa a primeira letra de cada palavra maiúscula
frase.strip()                        # exclui os espaços inúteis no início e no fim
frase.rstrip()                       # remove os primeiros espaços inúteis
frase.lstrip()                       # remove os últimos espaços inúteis
```

### Divisão e Junção
```python
frase.split()            # divide a string em palavras
'-'.join(frase)          # junta caracteres com hífens
```

---

✨ Aprendi bastante essa semana sobre bibliotecas, importações e como o Python trata strings. Que venha mais uma semana cheia de aprendizados!

