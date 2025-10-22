lista_mat = [[0,0,0], [0,0,0], [0,0,0]]
for l in range(0,3):
    for c in range(0,3):
        lista_mat[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
for linha in lista_mat:
    for v in linha:
        print(f'[ {v:^5} ]', end='')
    print()