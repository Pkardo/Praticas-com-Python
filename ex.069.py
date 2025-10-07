mais_18 = mulher_20 = homem_cadas= 0
while True:
    print('-'*20)
    print('CADASTRE UMA PESSOA')
    print('-' * 20)
    sexo = ' '
    idade = int(input('Idade: '))
    if idade >= 18: #contagem pessoas +18
        mais_18 += 1

    while sexo not in 'MF':
        sexo = str(input('Sexo[M/F]: ')).upper().strip()
    if idade <= 20 and sexo == 'F': #contagem mulher -20 anos
        mulher_20 += 1
    if sexo == 'M': #contagem homens cadastrados
        homem_cadas += 1

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar(?)[S/N]: ')).upper().strip()
    if continuar == 'N':
        print('-'*20)
        print('FIM DO PROGRAMA!')
        break

print(f'Total de pessoas +18 anos: {mais_18}\n'
      f'Ao todo foram {homem_cadas} homens cadastrados\n'
      f'E temos {mulher_20} mulheres com menos de 20 anos')