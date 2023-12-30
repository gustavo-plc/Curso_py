#EXERCÍCIO!!

primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

#como o input retorna string, para compará-las, 
#devo converter para números

primeiro_valor_int = int(primeiro_valor)
segundo_valor_int = int(segundo_valor)

if primeiro_valor_int > segundo_valor_int:
    maior_valor = primeiro_valor_int
    print(f'O maior é {maior_valor}')
elif primeiro_valor_int < segundo_valor_int:
    maior_valor = segundo_valor_int
    print(f'O maior é {maior_valor}')
else:
    print('Os valores são iguais!!')
