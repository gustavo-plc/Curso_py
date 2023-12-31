"""
fatiamento de strings
012345678 #ínices positivos da string
Olá mundo
-987654321 #índices negativos da string
fatiamento [i:f:p] [::] início, fim, passo

a função len retorna a quantidade de caracteres da str

"""

variavel = 'Olá mundo'
print(variavel[5])

#fatiamento
print(variavel[4:]) #quando quer fatiar até o fim, omite-se o fim
print(variavel[4:8]) #o índice final não é incluído.
print(variavel[:6])
print(variavel[-8:-2]) #usando os índices negativos

"""
contando o tamanho da string
"""
print(len(variavel)) #contagem de 
#caracteres usando len

#fazendo passo de 2 em 2
print(variavel[0:9:2]) 

#invertendo string (passo negativo)
print(variavel[::-1]) 





