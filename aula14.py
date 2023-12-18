#formatação de string com o método format

a = 'AAAAA'
b = 'BBBBBB'
c = 1.1
string = 'b={nome2} a={nome1} a={nome1} c={nome3:.2f}'
string_ini = 'a={0} b={1} c={2:.2f}'
formato = string_ini.format(a, b, c)
#tudo em python é um objeto, e objetos podem executar ações. Essas ações são chamadas de métodos. 
#
print(formato)

formato1 = string.format(
    nome1=a, nome2=b, nome3=c
)

print(formato1) 

#parâmetro nomeado é quando se dá nome às variáveis dentro da chamada das funções
#dentro do parenteses na chamada da função, os argumentos são os valores de cada variável assume, e os 
#parâmetros são as variáveis em si.

#quando uma função está dentro de um objeto, essa função é chamada de método.

#nome = "Luiz"
#idade = 23
#formato = '{n} tem {i} anos'
#print(formato.format(n=nome, i=idade))

