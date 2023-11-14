#Morse Code Trainer
#FROM UB6WBW

from playsound import playsound
from random import randint
from time import sleep


#cnt = symbols counter
cnt = 0
#Rand5 = array with group symbols
Rand5 = []
#MAX_SYMBOLS = limit of characters in a group
MAX_SYMBOLS = 5

print('-' * len('Morse code trainer'))
print ('Morse code trainer')
print('-' * len('Morse code trainer'), end = '\n\n')

while True:
    Rand5.append(chr(randint(48, 57)))
    cnt += 1
    if cnt%MAX_SYMBOLS == 0:
        cnt = 0
        for i in range(0, MAX_SYMBOLS):
            playsound('' + Rand5[i] + '.mp3')
        Input = '.'.join(input()).split('.')
            
        #Compare Input & Rand5
        if Input == Rand5:
            print('#'*len('Ok !'))
            print('Ok !')
            print('#'*len('Ok !'))
        else:
            print('#'*len('ERROR !'))
            print('ERROR !')
            print('#'*len('ERROR !'))
            
        #Print border
        print('#'* (2*MAX_SYMBOLS-1))
        
        for i in range(0, MAX_SYMBOLS):
            print(Rand5[i], end = ' ')
        print()
        
        #Print border
        print('#'* (2*MAX_SYMBOLS-1))
        print()
        print()
        sleep(3)
        Rand5.clear()
