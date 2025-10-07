from time import sleep
from pygame import mixer

for c in range(10, 0, -1):
    sleep(1)
    print(c)
sleep(1)
print('BOOOM, BOOOM, POW!')
mixer.init()
mixer.music.load('som_de_folgos.wav')
mixer.music.play(0)
sleep(7)