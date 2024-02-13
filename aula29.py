"""
Introdução ao try/except
try=> tentar executar o dódigo
except -> ocorreu algum erro ao tentar executar
"""

numero = input('Vou dobrar o número que vc digitar\n')
#uma função input SEMPRE retornará uma string. 
#Portanto, apesar de querer um número do usuário, o 4
# programa entenderá 
#o caractere como letra. 

print(f'O dobro de {numero} é {numero*2}')

#como corrigir? CASTING!

numero_float = float(numero)

print(f'O dobro de {numero_float} é {numero_float*2:.1f}')

print(123)
print(456)

#É SEMPRE NECESSPARIO TRATAR O INPUT DO USUÁRIO

print(numero.isdigit())

if numero.isdigit():
    print('Isso é um número inteiro')
else:
    print('Isso não é um número inteiro')

#o IF não evita exceções
    
try: 
    ...
    pass
except:
    ...
    