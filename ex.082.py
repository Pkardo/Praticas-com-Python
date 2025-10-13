listanum = []
lista_p = []
lista_i = []
while True:
    num = int(input('Digite um valor: '))
    listanum.append(num)
    if num % 2 == 0:
        lista_p.append(num)
    else:
        lista_i.append(num)
    duv = str(input('Quer continuar(?)[S/N]')).upper().strip()
    while duv not in 'SN':
        duv = str(input('Quer continuar(?)[S/N]')).upper().strip()
    if duv == 'N':
        break
print('-='*30)
print(f'A lista completa é: {listanum}')
print(f'A lista com números PARES é: {lista_p}')
print(f'A lista com números IMPARES é: {lista_i}')