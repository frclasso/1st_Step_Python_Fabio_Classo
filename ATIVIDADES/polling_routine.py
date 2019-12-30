#!/usr/bin/env python3

"""Polling for Piza to cure the hunger"""

import time

hungry = True

while hungry:
    print('\n'"Opening the front door")
    front_door = open("front_door.txt", 'r')

    if "Pizza Guy" in front_door:
        print("Pizza's here!")
        hungry = False
    else:
        print("Not yet...")

    print("Closing the front door")
    front_door.close()
    time.sleep(2)
print()
print('Done!!')