lista_p = list()
dados = list()
cont = 0
maior = 0
menor = 0
while True:
    dados.append(str(input('Nome: ')))
    while True:
        try:
            dados.append(float(input('Seu peso(Kg):')))
            break
        except ValueError:
            print(f'Erro, digite apenas número!')
    cont += 1
    duv = str(input('Quer continuar(?)[S/N]')).upper().strip()
    if cont == 1:
        maior = dados[1]
        menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    lista_p.append(dados[:])
    dados.clear()
    while duv not in 'SN':
        duv = str(input('Quer continuar(?)[S/N]')).upper().strip()
    if duv == 'N':
        print(f'Tivemos um total de {cont} pessoas cadastradas.')
        print(f'O maior peso foi {maior}Kg. Peso de ', end='')
        for v in lista_p:
            if v[1] == maior:
                print(f'[{v[0]}]', end=' ')
        print(f'\nO menor peso foi de {menor}Kg. Peso de ', end='')
        for v in lista_p:
            if v[1] == menor:
                print(f'[{v[0]}]', end=' ')
        break