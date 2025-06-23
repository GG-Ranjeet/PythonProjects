import random
import game_data
import art
from os import system


def game(name1, work1, place1, name2, work2, place2):
    print(f"Compare A: {name1}, a {work1}, from {place1}")
    print(art.vs)
    print(f"Compare B: {name2}, a {work2}, from {place2}\n\n")


info1 = 0
info2 = 0


def infogen(ing=0, info=0):
    while ing == info:
        if ing == 0:
            ing = random.choice(game_data.data)
        info = random.choice(game_data.data)
    info = random.choice(game_data.data)
    return ing, info


# print(info1) # cheats
# print(info2)

score = 0
on = True
while on:
    print(art.logo)
    if score != 0:
        print(f"You are right! current score {score}")
    info1, info2 = infogen(ing = info1,info = info2)
    # print(info1) #cheats
    # print(info2)
    game(info1["name"], info1["description"], info1["country"], info2["name"], info2["description"], info2["country"])
    guess = input("Who has more followers? Type 'A' or 'B': ")
    if guess in "bB":
        info1, info2 = info2, info1

    if info1["follower_count"] > info2["follower_count"]:
        score += 1
        info1, info2 = infogen(ing=info1, info=info2)
        system("cls")

    else:
        print(f"You lose You scored {score}")
        on = False

    


