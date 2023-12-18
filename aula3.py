'''
Python é uma linguagem de tipagem dinâmica e forte: 

- dinâmica: o python já sabe o tipo de informação
que estou passando para ele. print(1234), o PY já reconhece 
que esse argumento é um número inteiro;

- forte: 

Str=String=texto: é um trecho de texto que vai
dentro de aspas simples ou duplas

'''

print(1234) #numero inteiro
print('Texto dentro das aspas simples') #string
print("Texto dentro das aspas simples") #string

#escape: \

print("Texto dentro das aspas \"simples\"") #string com escapes: \
print(r"Texto dentro das aspas \"simples\"") #string com escapes: r: exibe o caractere de escape

#solução mais simples

print(1, 'Texto dentro das aspas "simples"') #aspas duplas dentro de aspas simples pode!(ou vice versa)
print(2, "Texto dentro das aspas 'simples'") #aspas duplas dentro de aspas simples pode!(ou vice versa)



