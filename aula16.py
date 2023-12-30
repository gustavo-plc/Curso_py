#operações condicionais (if-else)

#altera o fluxo do código

entrada = input('Você quer "entrar" ou "sair"? ')

if entrada == 'entrar':
    print('Você entrou no sistema') #a identação faz toda a diferença
elif entrada == 'sair': #usado caso se tenha mais de uma opção
    print('Você saiu do sistema')
else: #será sempre a última opção
    print('Você não digitou nem entrar, nem sair!')

print('Fora dos BLOCOS!')

