#Morse Code Trainer
#FROM UB6WBW

from playsound import playsound
from random import randint
from time import sleep

cnt = 0
rnd = []
Rand5 = []
while True:
    rnd.append(randint(48, 57))
    rnd.append(randint(65, 90))
    Rand5.append(chr(rnd[randint(0,1)]))
    rnd.clear()
    cnt += 1
    if cnt%5 == 0:
        cnt = 0
        playsound('' + Rand5[0] + '.mp3')
        playsound('' + Rand5[1] + '.mp3')
        playsound('' + Rand5[2] + '.mp3')
        playsound('' + Rand5[3] + '.mp3')
        playsound('' + Rand5[4] + '.mp3')
        Input = '.'.join(input()).split('.')
        if Input == Rand5:
            print('#'*len('Ok !'))
            print('Ok !')
            print('#'*len('Ok !'))
        else:
            print('#'*len('ERROR !'))
            print('ERROR !')
            print('#'*len('ERROR !'))
        print('#'*9)
        print(Rand5[0], Rand5[1], Rand5[2], Rand5[3], Rand5[4])
        print('#'*9)
        print()
        print()
        sleep(3)
        Rand5.clear()
