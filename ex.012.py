produto = float (input('Qual é o preço do produto? '))

desc = (produto * 5) / 100
preco = produto - desc

print (f'O produto que custava R${produto:.2f}, na promoção com desconto de 5% vai custar R${preco:.2f}')

