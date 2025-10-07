print('Analisador de triãngulos')

t1 = float(input('Primeiro segmento: '))
t2 = float (input('Segundo segmento: '))
t3 = float (input('Terceiro segmento: '))

if t1 + t2 > t3 and t1 + t3 > t2 and t2 + t3 > t1:
    print(f'Os segmentos acima PODEM FORMAR um triângulo!')

    if t1 == t2 and t2 == t3 and t3 == t1:
        print('O triãngulo formado é um EQUILÁTERO!')

    elif t1 == t2 or t2 == t3 or t1 == t3:
        print('O triângulo formado é um ISÓCELES!')

    elif t1 != t2 and t2 != t3 and t3 != t1:
        print('O triângulo formado é um ESCALENO!')
else:
    print('O segmentos acima NÃO PODEM formar um triângulo')