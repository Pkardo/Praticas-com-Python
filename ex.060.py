from math import factorial
num = int(input('Digite um número para\n'
      'calcular seu Fatorial: '))
fac = factorial(num)
print(f'Calculando !{num} = ', end='')
while num > 0:
    print(f'{num}', end=' ')
    num = num - 1
    if num > 0:
        print('x', end=' ')
print(f'= {fac}')
