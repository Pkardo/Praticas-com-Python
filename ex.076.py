print('-'*40)
print(f'{'LISTAGEM DE PREÇOS':^40}')
print('-'*40)
produtos = ('Lápis', 2.00,
         'Borracha', 3.00,
         'Caderno', 10.50,
         'Estojo',25.00,
         'Transferidor',4.20,
         'Compasso',9.99,
         'Mochila',119.99,
         'Canetas',22.30)
for t in range(0, len(produtos)):
    if t % 2 == 0:
        print(f'{produtos[t]:.<30}R$', end='')
    else:
        print(f'{produtos[t]:>7.2f}')
print('-'*40)

