print('-'*25)
print('Sequência de Fibonacci')
print('-'*25)
n1 = 0
n2 = 1
cont = 0
termo = int(input('Quantos termos você quer mostrar(?): '))
while termo > cont:
    print(n1, end=' ➡ ')
    n_total = n1+n2
    n1 = n2
    n2 = n_total
    cont += 1
print('FIM')