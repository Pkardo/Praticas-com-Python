matriz = [[0,0,0], [0,0,0], [0,0,0]]
soma_c3 = soma_p = m = 0
for l in range(0,3): 
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor na posição [{l}, {c}]: '))
        soma_c3 += matriz[l][2] #faz a soma dos valores da terceira coluna
print('-='*30)
for linha in matriz: #cria uma variavel para todas as listas dentro da lista
    for v in linha: #percorre o valor unitário dentro de cada uma das listas
        print(f'[{v:^5}]', end='')
    print()
    for v in linha:
        if v % 2 == 0: #analisa se o número PAR
            p = v
            soma_p += p
m = max(matriz[1]) #faz o 'm' receber o maior valor da segunda linha
print('-='*30)
print(f'A soma de todos valores PARES é {soma_p}')
print(f'A soma dos valores da terceira coluna é {soma_c3}')
print(f'O maior valor da segunda linha é {m} ')