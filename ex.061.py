cont = 0
print('Gerador de PA')
print('-='*7)
termo = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))

while cont < 10:
        print(termo, end=' ➡ ')
        cont = cont + 1
        termo += razao
print('ACABOU!')




