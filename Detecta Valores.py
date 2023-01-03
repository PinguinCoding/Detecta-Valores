valores = list()
index_maior = []
index_menor = []
maior_valor = 0
menor_valor = 0
for cont in range(0, 5):
    valores.append(int(input(f'Insira um valor para posição {cont}: ')))

for index, value in enumerate(valores):
    if index == 0:
        maior_valor = value
        menor_valor = value

    if value > maior_valor:
        maior_valor = value

    if value < menor_valor:
        menor_valor = value

for index, value in enumerate(valores):
    if value == maior_valor:
        index_maior.append(index)
    if value == menor_valor:
        index_menor.append(index)

print('=-'*30)
print(f'Você digitou os valores {valores}')
print(f'O maior valor detectado foi {maior_valor}',end=' nas posições ')
for index in index_maior:
    print(f'{index}...', end='')
print(f'\nO menor valor detectado foi {menor_valor}', end=' nas posições ')
for index in index_menor:
    print(f'{index}...', end='')
