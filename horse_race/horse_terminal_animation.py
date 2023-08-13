import os
from time import sleep

from horse_art import running_horses

running_horses.reverse()


class animated_horse:
    def __init__(self, speed, race_len):
        self.speed = speed
        self.race_len = race_len

    def speed_to_delay(self):
        delay = 12 / self.speed * 0.3
        return delay

    def print_animation(self):
        for i in range(self.race_len):
            for j in range(0, len(running_horses) - 1):
                print(running_horses[j - 1])
                sleep(self.speed_to_delay())
                os.system("clear")


def main():
    animation1 = animated_horse(30, 10)
    animation1.print_animation()


if __name__ == "__main__":
    main()
