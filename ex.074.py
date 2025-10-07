from random import sample
'''aleatorios = sample(range(100),5)
print(f'Os valores sorteados foram: {aleatorios}')
cont = maior = menor = 0
for n in aleatorios:
    cont += 1
    if cont == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
print(f'O maior valor foi: {maior}')
print(f'O menor valor foi: {menor}')'''

'''aleatorios = sample(range(100),5)
print(f'Os valores sorteados foram: {aleatorios}')
maior = menor = aleatorios[0]
for n in aleatorios:
    if n > maior:
        maior = n
    if n < menor:
        menor = n
print(f'O maior valor foi: {maior}')
print(f'O menor valor foi: {menor}')'''

'''aleatorios = sample(range(100),5)
print(f'Os valores sorteados foram: {aleatorios}')
print(f'O maior valor foi: {max(aleatorios)}')
print(f'O menor valor foi: {min(aleatorios)}')'''

from random import randint
'''aleatorios = (randint(1,10), randint(1,10), randint(1,10), randint(1,10) , randint(1,10))
print(f'Os valores sorteados foram: {aleatorios}')
cont = maior = menor = 0
for n in aleatorios:
    cont += 1
    if cont == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
print(f'O maior valor foi: {maior}')
print(f'O menor valor foi: {menor}')'''

'''aleatorios = randint(1,100), randint(1,100), randint(1,100), randint(1,100), randint(1,100)
print(f'Os valores sorteados foram: ', end='')
for n in aleatorios:
    print(f'{n}', end=' ')
print(f'\nO maior valor sorteado foi: {max(aleatorios)}')
print(f'O menor valor sorteado foi: {min(aleatorios)}')'''