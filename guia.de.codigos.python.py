# === DICIONARIO DOS CODIGOS PYTHON ===

# Para mostrar a mensagem fixada na tela
print("Hello mundo")

# Retorna o texto ao usuario, E espera digitar algo!
# É comum armazenar a resposta em uma variável, como no exemplo abaixo:
resposta_usuario = input("Qual é o seu nome? ")
print("Olá,", resposta_usuario) # Exemplo de uso da resposta

# Variaveis: Guardam informações para serem usadas futuramente.
nome = "Johnny"
idade = 24  # Nota: idade é geralmente um número inteiro (int), não string "24"
altura = 1.87
peso = 76

# Exemplo de como usar uma variavel
print("Seu nome é:", nome)
print("Você tem", idade, "anos.")

# === === ===  === ===

       # ===Tipos de Dados===
         
       # Serve para organizar diferentes tipos de informação.

# número inteiro (ex: idade, quantidade)
inteiro = 10  

# número com casa decimal (float)
decimal = 3.14 

# texto (string)
texto = "Python" 

# verdadeiro ou falso (boolean)
booleano = True 

# vários valores em ordem (lista/array)
lista = [1, 2, 3, "maçã", True]

# como lista, mas imutável (não pode ser alterado depois de criado)
tupla = (1, 2, 3) 

# chave: valor (dicionário - para dados estruturados)
dicionario = {"nome": "Johnny", "idade": 20}
    
# === Verificando Tipos ===
# Para saber qual o tipo de dado de uma variável usamos 'type()'
print(type(inteiro)) # Isso imprime na tela: <class 'int'>
print(type(texto))   # Isso imprime na tela: <class 'str'>
    
    
          #=== === === === ===#
    
     #===Operadores Matematicos===#

           
# soma                    a + b        (ex: 5 + 3 = 8)    
# subtração               a - b        (ex: 10 - 4 = 6)
# multiplicação           a * b        (ex: 3 * 4 = 12)
# divisão exata           a / b        (ex: 10 / 3 = 3.33...)
# divisão inteira         a // b       (ex: 10 // 3 = 3)
# resto da divisão        a % b        (ex: 10 % 3 = 1)
# potência (ex: 2**3 = 8) a ** b       (ex: 2 ** 3 = 8)
           
   #==Operadores de comparação==#
#Usados em condições, loops e lógica geral.

# igual ("==")          (ex: 5 == 5 é True)
# diferente("!=" que é "! + =") (ex: 5 != 6 é True)
# maior que (">")       (ex: 5 > 6 é False)
# menor que ("<")       (ex: 5 < 6 é True)
# maior ou igual (">=" que é, "> + =")
# menor ou igual ("<=" que é, "< + =")

   #=== Operadores Logicos===#
   #usado para combinar ou negar condições

# e == and    (True and False resulta em False)
# ou == or    (True or False resulta em True)
# não == not  (not True resulta em False)


# === Condicionais (If / Elif / Else) ===
# Usado para executar código diferente dependendo de uma condição.

# Exemplo:
if idade >= 18 and peso >= 70:
    print("Você pode doar sangue, se atender a outros requisitos.")
elif idade >= 18:
    print("Você é maior de idade, mas verifique o peso.")
else:
    print("Você é menor de idade.")

# === DICIONARIO DOS CODIGOS PYTHON — PARTE 2 ===

# === Loops (Repetições) ===
# Usados para repetir ações várias vezes.

# === Loop FOR ===
# Executa um bloco de código um número definido de vezes, ou itera sobre itens de uma lista/sequência.

# range(5) cria uma sequência: 0, 1, 2, 3, 4
for i in range(5):  
    print("Número:", i)

# === Loop WHILE ===
# Repete ENQUANTO a condição especificada for verdadeira.

contador = 0 
while contador < 5: 
    print("Contador está em:", contador) 
    contador += 1  # adiciona +1 a cada repetição, para evitar loop infinito

# === Comandos de controle de Loop ===

# break → para o loop imediatamente, saindo dele.
for i in range(10): 
    if i == 5: 
        break  
    print("Valor antes do break:", i) # Imprime 0, 1, 2, 3, 4

# continue → pula para a próxima repetição imediatamente, ignorando o código abaixo dele.
for i in range(10): 
    if i % 2 == 0: 
        continue  # Pula os números pares (0, 2, 4, 6, 8)
    print("Número ímpar:", i) # Imprime 1, 3, 5, 7, 9

# === Funções ===
# Funções permitem criar blocos de código reutilizáveis e comandos personalizados.

def saudacao(): 
    print("Olá! Esta é uma função sem parâmetros.")

saudacao()  # Chamando (executando) a função

# Função com parâmetro (entrada de informação necessária para a função funcionar)
def apresentar(nome): 
    print("Prazer, meu nome é", nome)

apresentar("Johnny")

# Função com retorno (devolve valores para quem a chamou, usando 'return')
def somar(a, b): 
    return a + b

resultado = somar(5, 3) 
print("Resultado da soma:", resultado) # Imprime 8

# === Listas (Arrays) ===
# Estrutura que guarda vários valores (de diferentes tipos) em uma única variável, em ordem.

frutas = ["maçã", "banana", "uva"]

# Ações comuns:
frutas.append("laranja")     # adiciona item ao final da lista
frutas.remove("banana")      # remove a primeira ocorrência do item
print(frutas[0])             # acessa o primeiro elemento (índice começa em 0)
print(len(frutas))           # len() retorna a quantidade total de itens

# === Manipulação de Strings (Textos) ===

texto = "Python é incrível"

print(texto.upper())   # Tudo MAIÚSCULO
print(texto.lower())   # Tudo minúsculo
print(texto.title())   # Primeiras letras de cada palavra maiúsculas
print(texto.replace("incrível", "poderoso"))  # troca palavras/partes do texto
print(texto[::-1])     # texto invertido (técnica de slice com 'passo' -1)

# === Fatiamento de Strings (Slice) ===
# Acessando partes de sequências (strings, listas, tuplas)

nome = "Johnny"

print(nome[0:3])  # do índice 0 (incluído) até o 3 (excluído) → "Joh"
print(nome[2:])   # do índice 2 até o final → "hnny"
print(nome[:4])   # do início até o índice 4 (excluído) → "John"

# === Tratamento de Erros (Try / Except) ===
# Serve para prevenir que o programa pare de funcionar inesperadamente (erros controlados).

try: 
    numero = int(input("Digite um número: "))
    print("Você digitou:", numero)
except ValueError: 
    print("Erro: Você não digitou um número inteiro válido.")

# === Trabalhando com Arquivos ===
# Abrindo, lendo e escrevendo em arquivos no disco.

# Escrever em arquivo ("w" = write, sobrescreve o arquivo ou cria um novo):
with open("arquivo.txt", "w") as arquivo: 
    arquivo.write("Hello, arquivo!\n")
    arquivo.write("Segunda linha.\n")

# Ler de arquivo ("r" = read):
with open("arquivo.txt", "r") as arquivo: 
    conteudo = arquivo.read() 
    print("Conteúdo do arquivo:")
    print(conteudo)

# === Dicionários (Mapas/Objetos) ===
# Armazena dados em pares Chave: Valor (não ordenado, acesso via chave)

pessoa = {"nome": "Johnny", "idade": 24, "cidade": "São Paulo"}

# Acessar:
print(pessoa["nome"])      # Acessa o valor pela chave 'nome'

# Adicionar nova chave:
pessoa["altura"] = 1.87

# Alterar valor de chave existente:
pessoa["idade"] = 25

# Remover chave e valor:
del pessoa["cidade"]

# === Estruturas de Dados Avançadas ===

# Conjuntos (Set) → coleção de valores únicos e não ordenados (remove duplicatas automaticamente)
conjunto = {1, 2, 2, 3, 4} 
print(conjunto)  # imprime: {1, 2, 3, 4}

# === List Comprehension ===
# Maneira rápida e "Pythonica" de criar listas com uma única linha de código.

# Cria uma lista de quadrados dos números de 0 a 9
quadrados = [x**2 for x in range(10)] 
print(quadrados) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# === Funções Lambda (funções anônimas, pequenas e rápidas) ===

dobro = lambda x: x * 2 
print(dobro(5))  # resultado: 10

# === Programação Orientada a Objetos (POO) ===
# Criando classes (moldes) e objetos (instâncias)

class Pessoa: 
    # Método inicializador (__init__) que roda quando o objeto é criado
    def __init__(self, nome, idade): # CORREÇÃO: Usar __init__ (duplo underscore)
        self.nome = nome
        self.idade = idade

    # Outro método (função da classe)
    def falar(self):
        print(self.nome, "está falando...")

# Criando um objeto (instância) da classe Pessoa
p1 = Pessoa("Johnny", 24) 
p1.falar() # Chamando o método do objeto

# === Módulos e Bibliotecas ===
# Reutilizando código que outras pessoas escreveram.

import math # Módulo nativo do Python
print(math.sqrt(81))  # sqrt() calcula a raiz quadrada -> 9.0

# === Consumindo API (Requisições Web) ===

# NOTA: Requer instalação prévia via terminal/prompt de comando: pip install requests
import requests 

# Exemplo de requisição GET simples:
resposta = requests.get("https://api.github.com") 
print(resposta.status_code) # Código HTTP (ex: 200 OK)
print(resposta.json())      # Converte a resposta JSON em um dicionário Python

