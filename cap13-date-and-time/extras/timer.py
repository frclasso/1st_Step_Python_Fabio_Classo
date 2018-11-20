#!/usr/bin/env python3

# Criando um  timer

#exemplo 1
import time

# print("Start:  %s" % time.ctime())
#
# time.sleep(5)
# print("End:  %s" % time.ctime())


# exemplo 2

seconds = 4
while seconds != 0:
    print(f"Voce tem {seconds} segundos para respoder...")
    time.sleep(2)
    seconds -=1
print('Game Over, You Will Die!')
