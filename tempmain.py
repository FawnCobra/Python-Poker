import random
import config
import easytable as debug

class User:
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
        playerlist.append(User(f'player{x}', [], 0, 50, 0))
    return playerlist

# deals any specified amount of cards to the player from the top of the deck and removes it
def card_deal(player:User, cardamnt:int, deck:list[str]):
    temp = deck[0:cardamnt]
    del deck[0:cardamnt]
    player.cards += temp
    # returns the new deck of cards since modified, returns the player object with new cards
    return deck, player

# returns a int of the current highest bet
def get_highest_bet(playerlist: list[User]) -> int:
    highestbet = 0
    for i in range(len(playerlist)):
        if playerlist[i].bet >= highestbet:
            highestbet = playerlist[i].bet
    return highestbet


def bet_round(playerlist: list[User]) -> list[User]:
    betlist = []
    currentbet = get_highest_bet(playerlist)
    for _ in playerlist:
        betlist.append(_.bet)
    while all(elem == betlist[0] for elem in betlist) == False or currentbet == 0:
        for _ in playerlist:
            betlist.append(_.bet)
        for player in playerlist:
            currentbet = get_highest_bet(playerlist)
            if player.status != 1 or 3:
                if player.bet == currentbet:
                    print(f'|{player.name}|current bet:{currentbet}| you currently make the current bet would you like to add to your bet, fold')
                    print("type 'A' for add or type 'F' for fold")
                    response = input().upper()
                    while response not in ['A','F']:
                        response = input().upper()
                    if response == 'A':
                        betamount = int(input(f'|{player.name}|bal:{player.balance}|how much would you like to add to your bet? '))
                        while (betamount < config.minbet) or (betamount >= (player.balance + 1)):
                            if betamount < config.minbet:
                                print("bet needs a min of 10")
                                betamount = int(input(f"{player.name} how much would you like to bet? "))

                            # checks if bet is higher than balance
                            if betamount >= (player.balance + 1):
                                print("bet needs to be less than your bal")
                                betamount = int(input(f"{player.name} how much would you like to bet? "))

                        player.bet += betamount
                        player.balance -= betamount
                    elif response == 'F':
                        player.status = 3
                elif (player.balance + player.bet) >= currentbet:
                    print(f"|{player.name}|you dont have enough to match the bet would you like to go all in or fold? ")
                    print("type 'A' for all in or type 'F' for fold")
                    response = input().upper()
                    while response not in ['A','F']:
                        print(response)
                        response = input().upper()
                    # if player chooses all in, dumps balance into bet and changes status to 1(all in)
                    if response == 'A':
                        player.bet += player.balance
                        player.balance = 0
                        player.status = 1
                    # if player chooses fold, changes status to 3(fold)
                    elif response == 'F':
                        player.status = 3
            elif player.status == 1:
                print(f"|{player.name}| You are all. Would you like to fold? ")
                response = input("'Y' for yes or 'N' no")
                while response not in ['Y','N']:
                    response = input().upper()
                if response == 'Y':
                    player.status = 3


if __name__ == "__main__":
    deck = shuffle(config.gamedeck)
    playerlist = newtable()
    for i in range(len(playerlist)):
        deck, playerlist[i] = card_deal(playerlist[i], 2, deck)
    
    
        # players turn to add bets
    playerlist = bet_round(playerlist)
    