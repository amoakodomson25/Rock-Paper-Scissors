import random


def play():
    user = input("'r' for rock, 'p' for paper & 's' for sccisors\n")
    computer = random.choice(["r", "p", "s"])

    if user == computer:
        return "tie"

    if won(user, computer):
        return "you won"
    return "you lost"


def won(player, opponent):
    if (
        (player == "r" and opponent == "s")
        or (player == "p" and opponent == "r")
        or (player == "s" and opponent == "P")
    ):
        return True


print(play())
