class Horse:
    def __init__(self, name, speed, colour):
        self.name = name
        self.speed = speed
        self.colour = colour


h1 = Horse("Batory", 0.10, "Chestnut")

print(f"{h1.name}, {h1.speed}, {h1.colour}")
