listanum = []
cont = 0
while True:
    for n in listanum:
        novo_valor = n
        if novo_valor in listanum:
            print('Esse número já foi adicionado.')
        else:
            listanum.append(novo_valor)
    listanum.append(int(input('Digite um valor: ')))
    print(f'Valor adicionado com sucesso...')
    duv = ' '
    while duv not in 'SN':
        duv = str(input('Quer continuar(?)[S/N]: ')).upper().strip()
    if duv == 'N':
        break
print(f'{sorted(listanum)}')