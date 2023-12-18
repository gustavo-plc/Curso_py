a = 'AAAAA'
b = 'BBBBBB'
c = 1.1
string = 'b={nome2} a={nome1} a={nome1} c={nome3:.2f}'
string_ini = 'a={} b={} c={}'
formato = string_ini.format(a, b, c)
#tudo em python é um objeto, e objetos podem executar ações. Essas ações são chamadas de métodos. 
#
print(formato)

#formato = string.format(
#    nome1=a, nome2=b, nome3=c
#)

