from horse_art import running_horses
from time import sleep
import os

running_horses.reverse()

def animated_horse(iterations):
    for i in range(iterations):
        for j in range(0,5):
            print(running_horses[j-1])
            sleep(0.15)
            os.system('clear')

animated_horse(10)
