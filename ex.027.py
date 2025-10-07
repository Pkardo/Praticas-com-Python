nome = str (input ('Digite seu nome completo: ')).strip()

print(f'Muito prazer te conhecer!\n'
      f'Seu primeiro nome é {nome.split()[0]}\n'
      f'Seu último nome é {nome.split()[-1]}')