import random

card_in_a_deck = [[1,11], 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player = []
opponent = []

def card_shuffle():
    num_of_deck = 4
    cards = []
    for i in range(num_of_deck):
        cards +=card_in_a_deck
    random.shuffle(cards)
    return cards

cards = card_shuffle()

def sum(x):
    total = 0
    for item in x:
        if type(item) == list:
            total += item[1]
            if total>21:
                total-=10  
        else:
            total += item
    return total


def details():
    print(cards)
    print(len(cards))
    print(f"player holding: {player} total score: {sum(player)}")
    print(f"Opponent holding: {opponent}")
details()


def assign(you, them, card):
    you.append(card.pop())
    them.append(card.pop())
    you.append(card.pop())
    them.append(card.pop())
    return you,them,card


def bust_check_player(x,y,z, play = "y"):
    x.append(z.pop())

    print(f"You holding: {x}, current score: {sum(x)}")
    print(f"Opponent's first card: {y[0]}")
    if not sum(x) > 21:
        draw = input("Type y to get another card or Type n to pass: ")
        if draw =="y":
            bust_check_player(x,y,z)
        else:
            print(x,y,z)
            return x,y,z,play
    else:
        print("You are busted!")
        x = []
        y = []
        play = input("Do u want to play BlackJack y/n: ")
        return x,y,z,play


def bust_check_op(x,y,z, play = "y"):
    x.append(z.pop())
    print(f"opponent holding {x} total score: {sum(x)}")
    if sum(x)<=13:
            bust_check_op(x,y,z)
    elif (13<sum(x)<=21):
        print(x,y,z)
        return x,y,z,play
    else:
        print("Opponent Busted, YOU WON!!")
        x = []
        y = []
        play = input("Do u want to play BlackJack y/n: ")
        return x,y,z,play


play = input("Do u want to play BlackJack y/n: ")

while play =="y":
    player, opponent, cards = assign(player, opponent, cards)
    print(f"You holding: {player} total score: {sum(player)}")
    print(f"Opponent's first card: {opponent[0]}")
    
    draw = input("Type y to get another card or type n to pass: ")
    if draw == 'y':
        player, opponent, cards, play = bust_check_player(player,opponent,cards)

    elif draw == 'n':
        print(f"opponent holding {opponent} total score: {sum(opponent)}")

        if sum(opponent)<=13:
            opponent, player, cards, play = bust_check_op(opponent,player,cards)
        elif 13<sum(opponent)<=21:
            if sum(opponent)< sum(player):
                print("Congratulation you won!")
                player = []
                opponent = []
                play = input("Do u want to play BlackJack y/n: ")
            else:
                print("You lose")
                player = []
                opponent = []
                play = input("Do u want to play BlackJack y/n: ")
        else:
            print("Opponent Busted, You won lol XD")
            player = []
            opponent = []
            play = input("Do u want to play BlackJack y/n: ")
