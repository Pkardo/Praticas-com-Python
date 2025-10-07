s = 0
print('='*25)
print('   10 TERMOS DE UMA PA   ')
print('='*25)
primeiro_t = int (input('Primeiro Termo: '))
razao = int (input('Razão: '))

for t in range(primeiro_t, primeiro_t + (razao *10), razao):
    print(t, '➙', end=' ')
print('ACABOU')