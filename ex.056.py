soma_idade = 0
maior_idade = 0
nome_velho = ''
soma_mulheres = 0
for p in range(1,5):
    print(f'--- {p} PESSOA ---')
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    soma_idade += idade
    sexo = str(input('Sexo(M/F): ')).upper()

    if p == 1 and sexo == 'M' and idade > maior_idade:
        maior_idade = idade
        nome_velho = nome
    elif sexo == 'M' and idade > maior_idade:
        maior_idade = idade
        nome_velho = nome

    if sexo == 'F' and idade <= 20:
        soma_mulheres += 1

media_idade = soma_idade / 4

print(f'A média de idade do grupo é de {media_idade} anos\n'
      f'O homem mais velho tem {maior_idade} anos e se chama {nome_velho}\n'
      f'Ao todo são {soma_mulheres} mulheres com menos de 20 anos')