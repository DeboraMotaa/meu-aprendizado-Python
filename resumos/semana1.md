# 🚀 Resumo de Estudos: Python – Curso em Vídeo

## 🌟 Técnicas de Estudo
- Utilizando o método **Pomodoro**:  
  2 ciclos de 25 minutos de estudo com 15 minutos de descanso entre eles.

---

## 📚 O que aprendi até agora

### 🧠 Conceitos Gerais
- Tudo em Python é um **objeto**: strings, listas, números, etc.
- Usar métodos e funções.
- A organização do código é essencial.
- Para **quebras de linha**, se usa `\n` (sem necessidade de abrir/fechar como no HTML).

---

### 🔍 Métodos úteis para strings
- `.islower()` – Verifica se o texto está todo em minúsculas.
- `.isupper()` – Verifica se está tudo em maiúsculas.
- `.isalnum()` – Verifica se é alfanumérico.
- `.isspace()` – Verifica se há apenas espaços.

🧩 Esses métodos são extremamente úteis, por exemplo, na **validação de senhas**.

---

# 🐍 Métodos e Funções Básicas em Python

## 🔤 Métodos de string (`str`)

| Método            | O que faz                                              | Exemplo                    |
|------------------|--------------------------------------------------------|----------------------------|
| `str.upper()`     | Converte todos os caracteres para maiúsculas          | `"oi".upper()` → `"OI"`   |
| `str.lower()`     | Converte todos os caracteres para minúsculas          | `"OI".lower()` → `"oi"`   |
| `str.capitalize()`| Capitaliza a primeira letra                           | `"python".capitalize()` → `"Python"` |
| `str.title()`     | Capitaliza a primeira letra de cada palavra           | `"bom dia".title()` → `"Bom Dia"` |
| `str.strip()`     | Remove espaços do início e fim                        | `" oi ".strip()` → `"oi"` |
| `str.replace()`   | Substitui partes da string                            | `"Olá mundo".replace("mundo", "Python")` → `"Olá Python"` |
| `str.find()`      | Retorna o índice de um trecho                         | `"banana".find("na")` → `2` |
| `str.isnumeric()` | Verifica se é composto só por números                 | `"123".isnumeric()` → `True` |
| `str.isalpha()`   | Verifica se é composto só por letras                  | `"abc".isalpha()` → `True` |
| `str.isalnum()`   | Verifica se é composto por letras e/ou números        | `"abc123".isalnum()` → `True` |
| `str.isspace()`   | Verifica se tem apenas espaços                        | `"   ".isspace()` → `True` |
| `str.islower()`   | Verifica se está tudo em minúsculo                    | `"abc".islower()` → `True` |
| `str.isupper()`   | Verifica se está tudo em maiúsculo                    | `"ABC".isupper()` → `True` |
| `str.istitle()`   | Verifica se está capitalizada                         | `"Bom Dia".istitle()` → `True` |

## 🔢 Funções úteis do Python

| Função          | O que faz                                   | Exemplo                        |
|----------------|----------------------------------------------|--------------------------------|
| `print()`       | Exibe informações no console                 | `print("Oi")` → `Oi`           |
| `type()`        | Mostra o tipo de dado                        | `type(10)` → `<class 'int'>`  |
| `len()`         | Retorna o tamanho (número de caracteres)    | `len("Python")` → `6`         |
| `input()`       | Recebe entrada do usuário                   | `nome = input("Digite seu nome: ")` |

## 🧩 Outros elementos úteis

### 🔸 `\n` → Quebra de linha

- **O que é:** uma **sequência de escape** (*escape sequence*).
- **Serve para:** pular para uma nova linha dentro de uma string.
- **Exemplo:**

```python
print("Linha 1\nLinha 2")
```

---

## 💡 Observações pessoais
- Estou me divertindo durante os testes e até quando erro.
- Aprender o nome correto dos elementos está me ajudando a entender melhor o código, buscar por conteúdos mais precisos e acelerar o meu aprendizado!
- Ver o código funcionar é muito satisfatório!
- Estou aprendendo com a prática e os erros — e isso é parte essencial do processo.

---
