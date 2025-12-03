"""Introdução ao Python"
Este é um guia introdutório para Python, focando em exemplos práticos e dicas úteis para iniciantes.
"""

# Exemplo 1: Usando f-strings
print(f"O resultado é: {resultado}")  # Substitui prints de concatenação por f-string

# Exemplo 2: Seções com comentários
"""Seção A: Estruturas de Dados"""

# Aviso sobre input() em Jupyter
# """ Cuidado ao usar input() em Jupyter! Pode causar um comportamento inesperado. """

# Exemplo 3: Funções Lambda com List Comprehension
pares = [x for x in range(10) if (lambda x: x % 2 == 0)(x)]

# Exemplo 4: Dicionários
meu_dict = {
    'Nome': 'Alice',
    'Idade': 30,
    'Cidade': 'São Paulo'
}

# Usando métodos de dicionário
print(meu_dict.keys())   # Mostra as chaves
print(meu_dict.values()) # Mostra os valores
print(meu_dict.items())  # Mostra pares chave-valor
print(meu_dict.get('Nome'))  # Acessa o valor pela chave
