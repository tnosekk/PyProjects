import random


def play():
    user = input("'r' for rock, 'p' for paper, 's' for scissors: ")
    computer = random.choice(["r", "p", "s"])

    if user == computer:
        return "Tie"

    if is_win(user, computer):
        return "You won!"

    return "You lost!"


def is_win(player, opponent):
    # returns True if player wins
    if (
        (player == "r" and opponent == "s")
        or (player == "s" and opponent == "p")
        or (player == "p" and opponent == "r")
    ):
        return True
    else:
        return False


if __name__ == "__main__":
    print(play())
