'''soma = 0
exp = input('Digite sua expressão: ')
for c in exp:
    if '(' == c:
        soma += 1
    if ')' == c:
        soma -= 1
    if soma == -1:
        break
if soma == 0:
    print(f'Expressão CORRETA!')
else:
    print(f'Expressão INVÁLIDA!')'''
