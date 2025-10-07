lista_num = []
maior = 0
menor = 0
for c in range(0,5):
    lista_num.append(int(input(f'Digite o valor na posição {c}: ')))
    if c == 0:
        maior = menor = lista_num[c]
    else:
        if lista_num[c] > maior:
            maior = lista_num[c]
        if lista_num[c] < menor:
            menor = lista_num[c]
print('-='*30)
print(f'Os valores digitados foram {lista_num}')
print(f'O maior número foi {maior} nas posições ', end='')
for pos, valor in enumerate(lista_num):
    if valor == maior:
        print(f'{pos}...', end='')
print(f'\nO menor número foi {menor} nas posições ', end='')
for pos, valor in enumerate(lista_num):
    if valor == menor:
        print(f'{pos}...', end='')