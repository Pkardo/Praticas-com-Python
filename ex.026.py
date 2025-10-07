frase = str (input('Digite uma frase que possua letra "A": ')).strip().upper()

frase= frase.replace('Á','A')
frase= frase.replace('Ã','A')
frase= frase.replace('Â','A')

print(f'Na sua frase podemos identificar um total de {frase.count('A')} "A" \n'
      f'A primeira letra "A" aparece na posição: {frase.find('A')+1}\n'
      f'A última letra "A" aparece na posição: {frase.rfind('A')+1}')