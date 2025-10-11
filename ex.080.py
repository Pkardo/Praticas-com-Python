listaval = []
for c in range(0,5):
    n = int(input(f'Valor {c}: '))
    if c == 0 or n > listaval[-1]:
        listaval.append(n)
    else:
        cont = 0
        while cont < len(listaval):
            if n <= listaval[cont]:
                listaval.insert(cont,n)
                break
            cont += 1
print(listaval)