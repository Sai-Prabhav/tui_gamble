import random

total = 1_00_000


def toss():
    bet = int(input("Enter the amount you like to bet: "))
    choice = int(input("0. Heads\n1. Tails\n>"))
    flip = random.choice([0, 1])
    print(f"The coin fliped {'heads' if flip else 'tails'}")
    if flip == choice:
        print(f"you win {bet*2}")
        return bet * 2
    else:
        print(f"you lost {bet}")
        return -bet


games = [("Toss a coin", toss)]


def play_game():
    global total
    print(f"you have a total of {total}$")
    print("Which game you like to play? (enter the number)")
    for n, key in enumerate(games):
        print(f"{n+1}. {key[0]}")
    game = games[int(input("> ")) - 1][1]
    total += game()


while total > 0:
    play_game()
