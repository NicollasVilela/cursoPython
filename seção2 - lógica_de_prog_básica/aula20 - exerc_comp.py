primeiro_valor = input('Valor 1: ')
segundo_valor = input('Valor 2: ')

x = int(primeiro_valor)
y = int(segundo_valor)

if x > y:
    print(f'O valor de X({x}) é maior que o valor de Y({y})!')
elif x < y:
    print(f'O valor de X({x}) é menor que o valor de Y({y})!')
else:
    print(f'O valor de X({x}) é igual ao valor de Y({y})!')
