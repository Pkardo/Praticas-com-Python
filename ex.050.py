from time import sleep
print('='*25)
print('Somador de números PARES')
print('='*25)
s = 0
cont = 0
for c in range(1,7):
    num = int(input('Digite um número:'))
    if num % 2 == 0:
        s += num
        cont += 1
    else:
        print('Analisando número..')
        sleep(0.5)
        print(f'Número Ímpar!')

print(f'A soma entre os {cont} números pares é igual a {s}.')