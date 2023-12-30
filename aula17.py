#if-elif-else

condicao1 = False
condicao2 = False
condicao3 = True
condicao4 = True

if condicao1:
    print('Este código pra a condicao 1')
    print('Este código pra a condicao 1')
elif condicao2:
    print('codigo para a condição 2')
elif condicao3:
    print('codigo para a condicao 3')
elif condicao4:
    print('cod para a cond 4') # por mais que a 4 seja verdadeira, 
    #ela não será nem checada, porque a 3 foi verdadeira antes, 
    #e fazia parte de um elif, ou seja, sairá do bloco.
else:
    print('nenhuma condicao foi satisfeita')

if 10 == 10:
    print('outro if') #if sozinho, de boa!

#elif e else só existem se existir um if!!

#else é sempre a última a ser executada.


print('Fora do if')