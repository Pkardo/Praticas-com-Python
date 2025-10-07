total_gasto = cont_1000 = cont = menor_preco = maior_preco = 0
menor_produto = ' '
while True:
    produto = str(input('Produto: '))
    preco = float(input('Valor: R$'))
    total_gasto += preco
    cont += 1
    if cont == 1 or preco < menor_preco:
        menor_preco = maior_preco = preco
        menor_produto = produto
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar(?)[S/N]: ')).upper().strip()
    if continuar == 'N':
        break
    if preco > 1000:
        cont_1000 += 1
print('---------FIM DO PROGRAMA---------')
print(f'O total gasto em compras foi R${total_gasto:.2f}\n'
      f'Temos {cont_1000} produto(s) acima de R$1000,00\n'
      f'E o produto mais barato foi ({menor_produto}) que custa R${menor_preco:.2f}')