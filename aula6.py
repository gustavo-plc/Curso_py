# conversão de tipos, coerção
# type convertion, typecasting, coercion
# é o ato de converter um tipo em outro
#  tipos imutáveis e primitivos:
# str, int, float, bool
# casting, no C

print(int('1'), type(int('1')))
print(type(float('1') + 1)) # a execução é de dentro pra fora!
print(bool(' '))
print(str(11) + 'b')