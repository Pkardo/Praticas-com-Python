s = 0
cont = 0
for imp in range(1, 501, 2):
    if imp % 3 == 0:
        s += imp
        cont += 1
print(f'A soma de todos os {cont} valores solicitados é {s}')
