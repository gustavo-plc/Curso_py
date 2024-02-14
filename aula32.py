"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

numero = input('Digite um número inteiro\n')

try: #ou utilizando o método isDigit()
    numero_inteiro = int(numero)
    print(f'O número inteiro digitado foi {numero_inteiro}')
    if numero_inteiro % 2 == 0:
        print(f'O número digitado é par!\n')
    else: 
        print(f'O número digitado é impar!\n')
except:
    print('Não foi digitado um número inteiro')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

hora_str = input('Digite a hora atual:\n') #todo retorno de input é string!

try:
    hora_num = int(hora_str)        
    if 0 <= hora_num <= 11:
        print(f'Bom dia!\n')
    elif 12 <= hora_num <= 17:
        print(f'Boa tarde!\n')
    else:
        print(f'Boa noite!\n')
except:
    print(f'Hora inválida!\n')


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('Favor digite seu primeiro nome:\n')


try: 
    nome_num = float(nome)
    print(f'Você digitou um número!')
except:
    if len(nome) <= 4: 
        print('Seu nome é curto!')
    elif len(nome) > 6: 
        print('Seu nome é muito grande!')
    else:
        print('Seu nome é normal!')