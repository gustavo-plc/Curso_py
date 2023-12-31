"""
Formatação básica de strings (ênfase em f-strings)
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda - preenche para a esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a 
"""

#isso não é tudo, mas o mais importante

variavel = 'ABC'
print(variavel)
print(f'{variavel}') #uso básico de f-strings
print(f'{variavel: >10}') #inserir largura fixa, caso a string não atinja
print(f'{variavel: <10}.')
print(f'{variavel: ^10}.')
print(f'{1000.4873648123746:0=+10,.1f}')
print(f'O hexadecimal de 1500 é {1500:08X}')
print(f'{variavel!r}')