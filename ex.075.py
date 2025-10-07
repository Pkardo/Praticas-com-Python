'''par = []
for n in range(1):
    valor1 = int(input('Digite um número: '))
    valor2 = int(input('Digite outro número: '))
    valor3 = int(input('Digite mais um número: '))
    valor4 = int(input('Digite o último número: '))
    tupla = (valor1, valor2, valor3, valor4)
    if valor1 % 2 == 0:
        par.append(valor1)
    if valor2 % 2 == 0:
        par.append(valor2)
    if valor3 % 2 == 0:
        par.append(valor3)
    if valor4 % 2 == 0:
        par.append(valor4)
    if 3 in tupla:
        print(f'O primeiro 3 está na {tupla.index(3)+1} posição.')
    print(f'O número 9 aparece {tupla.count(9)} vezes.\n'
    f'Os números pares foram {par}')'''

'''par = []
valor1 = int(input('Digite um número: '))
valor2 = int(input('Digite outro número: '))
valor3 = int(input('Digite mais um número: '))
valor4 = int(input('Digite o último número: '))
tupla = (valor1, valor2, valor3, valor4)
for n in tupla:
    if n % 2 == 0:
        par.append(n)
if 3 in tupla:
    print(f'O primeiro 3 está na {tupla.index(3)+1} posição.')
print(f'O número 9 aparece {tupla.count(9)} vezes.\n'
f'Os números pares foram {par}')'''

'''par = []
valor = (int(input('Digite um número: ')),
        int(input('Digite um número: ')),
        int(input('Digite um número: ')),
        int(input('Digite um número: ')),)
for n in valor:
    if n % 2 == 0:
        par.append(n)
if 3 in valor:
    print(f'O primeiro número 3 está na {valor.index(3)+1} posição.')
print(f'O número 9 aparece {valor.count(9)} vezes.\n'
      f'Os números PARES foram {par}')'''

num = (int(input('Digite um número: ')), int(input('Digite um número: ')),
                int(input('Digite um número: ')), int(input('Digite um número: ')))
print(f'Você digitou os valores {num}.')
if 3 in num:
    print(f'O primeiro 3 aparece na {num.index(3)+1} posição.')
print(f'O número 9 aparece {num.count(9)} vezes.\n'
      f'Os número PARES foram: ', end='')
for p in num:
    if p % 2 == 0:
        print(p, end=' ')