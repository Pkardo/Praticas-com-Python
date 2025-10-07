dinheiro = float (input('Quanto dinheiro você tem na sua carteira? '))
dollar = 5.62
euro = 6.40
francoS = 6.82
iene = 25.32
libra = 7.53
convert = dinheirso / dollar
convert2 = dinheiro / euro
convert3 = dinheiro / francoS
convert4 = dinheiro * iene
convert5 = dinheiro / libra

print (f'Com R${dinheiro} você pode comprar US${convert:.2f}\n'
       f'Com R${dinheiro} você pode comprar €UR${convert2:.2f}\n'
       f'Com R${dinheiro} você pode comprar CHF${convert3:.2f}\n'
       f'Com R${dinheiro} você pode comprar JP¥${convert4:.2f}\n'
       f'Com R${dinheiro} você pode comprar GPB£${convert5:.2f}')


