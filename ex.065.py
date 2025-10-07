pergunta = str('')
cont = soma = maior = 0
menor = 1000000
while pergunta != 'N':
    num = int(input('Digite um número: '))
    cont += 1 #contador
    soma += num #somador(num)
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    pergunta = str(input('Quer continuar? [S/N]: ')).upper().strip()
media = soma / cont
print(f'Você digitou {cont} números e a média foi {media:.2f}\n'
      f'O maior valor foi {maior} e o menor foi {menor}')