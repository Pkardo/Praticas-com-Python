nome = str (input('Digite seu nome: '))
primeiro_nome = (nome.split())
nome_todo = ''.join(primeiro_nome)
print (f'Analisando seu nome..\n'
       f'Seu nome em MAIÚSCULO fica: {nome.upper()}\n'
       f'Em minusculo fica: {nome.lower()}\n'
       f'Seu nome ao todo tem {len(nome_todo)} letras\n'
       f'Seu primeiro nome tem {len(primeiro_nome[0])} letras')

