listanum = []
maior = 0
menor = 0
for cont in range(0,5):
    listanum.append(int(input(f'Digite um valor na posição {cont}: ')))
    if cont == 0:
        maior = menor = listanum[cont]
    else:
        if listanum[cont] > maior:
            maior = listanum[cont]
        if listanum[cont] < menor:
            menor = listanum[cont]
print('-='*30)
print(f'Os valores que você digitou: {listanum}')
print(f'O maior valor foi {maior} e se encontra nas posições ', end='')
for p, valor in enumerate(listanum):
    if maior == valor:
        print(f'{p}...', end=' ')
print(f'\nO menor valor foi {menor} e se encontra nas posições ', end='')
for p, valor in enumerate(listanum):
    if menor == valor:
        print(f'{p}...', end=' ')