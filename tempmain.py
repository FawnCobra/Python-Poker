import random
import config
import easytable as debug

class user:
    def __init__(self, name: str, cards: list[str], status: int, balance: int, bet: int = 0):
        self.name = name
        self.cards = cards
        self.status = status
        self.balance = balance
        self.bet = bet

    def __str__(self):
        return f"{self.name}: ['cards': {self.cards}, 'status': {self.status}, 'balance': {self.balance}, 'bet': {self.bet}]"



# table = {"Dealer": {"cards": [], "status": 0}, "player1": {"cards": [], "status": 0}}
# status codes [0 = ready to play, 1 = all in, 3 = fold]

# shuffles the deck of cards
# ¯\_( ツ )_/¯ idk what else to say
def shuffle(deck):
    for i in range(len(deck)-1, 0, -1):
        j = random.randint(0, i + 1)
        deck[i], deck[j] = deck[j], deck[i]
    print("the deck has been shuffled")
    return deck

# produces a list of player objects depending on how many people are playing
def newtable():
    amount = input("how many players are gonna play ")
    # if nothing is input, it is assumed that 2 people are playing
    if amount == "":
        amount = "2"
    playerlist = []
    for x in range(int(amount)):
        playerlist.append(user(f'player{x}', [], 0, 50, 0))
    return playerlist

# deals any specified amount of cards to the player and removes it from the deck
def card_deal(player, cardamnt, deck):
    temp = deck[0:cardamnt]
    del deck[0:cardamnt]
    player.cards += temp
    return deck, player



if __name__ == "__main__":
    deck = shuffle(config.gamedeck)
    playerlist = newtable()
    for i in range(len(playerlist)):
        deck, playerlist[i] = card_deal(playerlist[i], 2, deck)
    