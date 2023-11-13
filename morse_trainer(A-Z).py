#Morse Code Trainer
#FROM UB6WBW

from playsound import playsound
from random import randint
from time import sleep

cnt = 0
Rand5 = []
MAX_SYMBOLS = 10

while True:
    Rand5.append(chr(randint(65, 90)))
    cnt += 1
    if cnt%MAX_SYMBOLS == 0:
        cnt = 0
        for i in range(0, MAX_SYMBOLS):
            playsound('' + Rand5[i] + '.mp3')
        Input = '.'.join(input()).split('.')
        if Input == Rand5:
            print('#'*len('Ok !'))
            print('Ok !')
            print('#'*len('Ok !'))
        else:
            print('#'*len('ERROR !'))
            print('ERROR !')
            print('#'*len('ERROR !'))
        print('#'* (2*MAX_SYMBOLS-1))
        for i in range(0, MAX_SYMBOLS):
            print(Rand5[i], end = ' ')
        print()
        print('#'* (2*MAX_SYMBOLS-1))
        print()
        print()
        sleep(3)
        Rand5.clear()
