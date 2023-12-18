#Função print já imprime
# cada argumento separado por
# espaço e também
# já insere a quebra de linha por padrão

#é possível usar argumentos nomeados, como sep e end, para alterar a forma
#padrão como a função separa os argumentos e termina a linha 

#python é case sensitive

print(12, 34, sep="-", end='\n##\n') #começa com argumentos não nomeados e seguem argumentos nomeados (sep, end)
print(56, 78, sep='#', end="\n") #usando o separador e o end
print(9, 10, sep='+', end='\n') 

# \r\n = CRLF