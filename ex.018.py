import math
angulo = float (input('Digite qualquer valor de angulo: '))
novo_angulo = math.radians(angulo)
print(f'O valor de seno é {math.sin(novo_angulo):.2f}\n'
      f'O valor do cosseno é {math.cos(novo_angulo):.2f}\n'
      f'O valor da tangente é {math.tan(novo_angulo):.2f}')