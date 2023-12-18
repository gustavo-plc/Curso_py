nome = 'Gustavo Cunha'
altura = 1.70
dinheiro = 10000.98
peso = 73
imc = peso/(altura**2)

#"f-Strings"
linha_1 = f'{nome} tem {altura:.2f} de altura' 
linha_2 = f'pesa {peso} quilos e seu IMC é'
linha_3 = f'{imc:.2f}' 


linha_4 = f'{nome} tem {dinheiro:,.2f} de dinheiro' #fstring

# esse f antes da string habilita a 
# possibilidade de usar variáveis dentro do texto
# da string 

# para pegar o valor das variáveis
# basta envolvê-las em chaves

# chama variáveis dentro da string

print(linha_1)
print(linha_2)
print(linha_3)


print(linha_4)
