maior_peso = 0
menor_peso = 1000000
for peso in range(1,6):
    peso_kg = float (input(f'Peso da {peso} pessoa: '))

    if peso_kg > maior_peso:
        maior_peso = peso_kg

    if peso_kg < menor_peso:
        menor_peso = peso_kg

print(f'O maior peso lido foi {maior_peso}KG\n'
      f'O menor peso lido foi {menor_peso}KG')