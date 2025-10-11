listanum = []
cont = 0
while True:
    num = int(input('Digite um valor: '))
    if num in listanum:
        print(f'Esse valor já foi digitado')
    else:
        listanum.append(num)
        print(f'Valor adicionado com sucesso...')
    duv = ' '
    while duv not in 'SN':
        duv = str(input('Quer continuar(?)[S/N]: ')).upper().strip()
    if duv == 'N':
        break
print(f'{sorted(listanum)}')