import random


class Horse:
    def __init__(self, name, speed, color):
        self.name = name
        self.speed = speed
        self.color = color

    def print_horse(self):
        print(f"Horse Name: {self.name}")
        print(f"Horse Speed: {self.speed}")
        print(f"Horse color: {self.color}")


h1 = Horse("Batory", random.randint(10, 50), "Chestnut")

h1.print_horse()
