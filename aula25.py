"""
interpolação básica de variáveis
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""

#formas básicas de escrever com print
#1. Format
#2. f-strings
#3. interpolação

#escolha uma e seja feliz!

nome = 'Luiz'
preco = 1000.95897643
variavel = '%s, o preço é R$ %.2f' % (nome, preco)
print(variavel) 
print('O hexadecimal de %d é %08x' % (1500000, 1500000))