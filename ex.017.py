'''from math import sqrt
cateto_oposto = float (input('Digite o Cateto: '))
cateto_adjacente = float (input ('Digite o Adjacente:'))

hipotenusa = cateto_oposto ** 2 + cateto_adjacente ** 2

print (f'O valor da sua Hipotenusa é {sqrt (hipotenusa):.2f}')'''
'''


co = float (input('Digite o Cateto: '))
ca = float (input('Digite o Adjacente: '))
hipotenusa = (co ** 2 + ca ** 2) ** 0.5
print(f'Sua Hipotenusa é igual a {hipotenusa:.2f}')'''


from math import hypot
co = float (input ('Digite o Cateto: '))
ca = float (input ('Digite o Adjacente:'))
hipotenusa =  hypot(co, ca)
print (f'A Hipotenusa vai medir {hipotenusa:.2f}')


