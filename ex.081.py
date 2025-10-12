listanum = []
while True:
    listanum.append(int(input('Digite um valor na posição: ')))
    lista_d = sorted(listanum, reverse=True)
    duv = str(input('Quer continuar(?)[S/N]')).upper().strip()
    while duv not in 'SN':
        duv = str(input('Quer continuar(?)[S/N]')).upper().strip()
    if duv == 'N':
        print(f'Lista em ordem DECRESCENTE: {lista_d}')
        print(f'Foram digitados ao todo {len(listanum)} números.')
        if 5 in listanum:
            print(f'O valor 5 faz parte da lista!')
            print(f'Em ordem DECRESCENTE, o valor 5 está na posição: ', end=' ')
            for p, v in enumerate(lista_d):
                  if v == 5:
                    print(f'{p+1}..', end='')
            print(f'\nNa ordem escrita o 5 está na posição: ', end=' ')
            for p, v, in enumerate(listanum):
                if v == 5:
                    print(f'{p+1}..', end=' ')
        else:
            print(f'O valor 5 não está na lista!')
        break