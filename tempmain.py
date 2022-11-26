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
def shuffle(deck:list[str]):
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

# deals any specified amount of cards to the player from the top of the deck and removes it
def card_deal(player:user, cardamnt:int, deck:list[str]):
    temp = deck[0:cardamnt]
    del deck[0:cardamnt]
    player.cards += temp
    # returns the new deck of cards since modified, returns the player object with new cards
    return deck, player

# promts the player to bet
def add_bet(playerlist: list[user], player:user):
    print(f"|current highest bet is {get_highest_bet(playerlist)}|")
    betamount = int(input(f"{player.name} how much would you like to bet? "))
    # keeps person in loop till bet ammount is both higher than the minumum bet and lower than their balance
    while (betamount < config.minbet) or (betamount >= (player.balance + 1)):

        # checks if bet is lower than min bet
        if betamount < config.minbet:
            print("bet needs a min of 10")
            betamount = int(input(f"{player.name} how much would you like to bet? "))
        # checks if bet is higher than balance
        if betamount >= (player.balance + 1):
            print("bet needs to be less than your bal")
            betamount = int(input(f"{player.name} how much would you like to bet? "))
    
    # when conditons are met the balance and bet will be adjusted accordingly
    player.bet += betamount
    player.balance -= betamount
    return playerlist

# returns a int of the current highest bet
def get_highest_bet(playerlist: list[user]):
    highestbet = 0
    for i in range(len(playerlist)):
        if playerlist[i].bet >= highestbet:
            highestbet = playerlist[i].bet
    return highestbet


if __name__ == "__main__":
    deck = shuffle(config.gamedeck)
    playerlist = newtable()
    for i in range(len(playerlist)):
        deck, playerlist[i] = card_deal(playerlist[i], 2, deck)
    
        # players turn to add bets
    for i in range(len(playerlist)):
        playerlist = add_bet(playerlist, playerlist[i])
