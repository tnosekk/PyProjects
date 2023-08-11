import os
from time import sleep

from horse_art import running_horses

running_horses.reverse()


def animated_horse(iterations, speed):
    speed = 12 / speed * 0.5
    for i in range(iterations):
        for j in range(0, len(running_horses) - 1):
            print(running_horses[j - 1])
            sleep(speed)
            os.system("clear")


def main():
    animated_horse(10, 60)


if __name__ == "__main__":
    main()
