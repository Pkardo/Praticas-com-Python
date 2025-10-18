'''lista_ini = list()
lista_par = list()
lista_impar = list()
for c in range(1,8):
    n = int(input(f'Digite o {c}nº valor: '))
    if n % 2 == 0:
        lista_par.append(n)
    else:
        lista_impar.append(n)
lista_par.sort()
lista_impar.sort()
lista_ini.append(lista_par[:])
lista_ini.append(lista_impar[:])
print(f'Os números PARES digitados foram: {lista_ini[0]}')
print(f'Os números ÍMPARES digitados foram: {lista_ini[1]}')'''

'''lista_n = [[], []]
for c in range(1,8):
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        lista_n[0].append(n)
    else:
        lista_n[1].append(n)
lista_n[0].sort()
lista_n[1].sort()
print(f'Os números PARES digitados foram: {lista_n[0]}')
print(f'Os números ÍMPARES digitados foram: {lista_n[1]}')'''