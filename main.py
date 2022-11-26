import random
import config
import easytable as debug




# table = {"Dealer": {"cards": [], "status": 0}, "player1": {"cards": [], "status": 0}}
# status codes [0 = ready to play, 1 = all in, 3 = fold, 4 = blackjack]

def shuffle(deck):
    for i in range(len(deck)-1, 0, -1):
        j = random.randint(0, i + 1)
        deck[i], deck[j] = deck[j], deck[i]
    print("the deck has been shuffled")
    return deck

def card_deal(playerhands, player, cardamnt, deck):
    inithand = deck[0:cardamnt]
    del deck[0:cardamnt]
    for card in inithand:
        playerhands[player]["cards"].append(card)  
    return deck, playerhands

def card_return(deck, playerhands):
    for player in playerhands:
        for cards in playerhands[player]["cards"]:
            if type(cards) is list:
                for card in cards:
                    deck.append(card)
            else:
                deck.append(cards)
            playerhands[player]["cards"] = []
            playerhands[player]["status"] = 0
    return deck, playerhands

def newtable():
    players = input("how many players are gonna play ")
    if players == "":
        players = "2"
    playerhands = {}
    for x in range(int(players)):
        playerhands.update({f"player{x}": {"cards": [], "status": 0,"balance": 50, "bet": 0,}})
    return playerhands

def add_bet(playerhands, player):
    print(f"|current highest bet is {get_highest_bet(playerhands)}|")
    betamnt = int(input(f"{player} how much would you like to bet? "))
    # keeps person in loop till bet ammount is both higher than the minumum bet and lower than their balance
    while (betamnt < config.minbet) or (betamnt >= (playerhands[player]["balance"] + 1)):

        # checks if bet is lower than min bet
        if betamnt < config.minbet:
            print("bet needs a min of 10")
            betamnt = int(input(f"{player} how much would you like to bet? "))
        # checks if bet is higher than balance
        if betamnt >= (playerhands[player]["balance"] + 1):
            print("bet needs to be less than your bal")
            betamnt = int(input(f"{player} how much would you like to bet? "))
    
    # when conditons are met the balance and bet will be adjusted accordingly
    playerhands[player]["bet"] = playerhands[player]["bet"] + betamnt
    playerhands[player]["balance"] = playerhands[player]["balance"] - betamnt
    return playerhands


def get_highest_bet(playerhands: dict[str, dict]):
    highestbet = 0
    for people in playerhands:
        if playerhands[people]["bet"] >= highestbet:
            highestbet = playerhands[people]["bet"]
    return highestbet

def match_bet(playerhands, player):
    highestbet = get_highest_bet(playerhands)
    
    if playerhands[player]["bet"] != highestbet:
        if (playerhands[player]["balance"] + playerhands[player]["bet"]) >= highestbet:
            bal = playerhands[player]["balance"]
            currentbet = playerhands[player]["bet"]
            print(f"|{player}|You need to match to the current bet of {highestbet}")
            betadd = int(input(f"|bet:{currentbet}|bal:{bal}|How much would you like to add to your bet? "))
            playerhands[player]["bet"] += betadd
            playerhands[player]["balance"] -= betadd

        else:
            print(f"|{player}|you dont have enough to match the bet would you like to go all in or fold?")
            print("type 'A' for all in or type 'F' for fold")
            response = input().upper()
            while response not in ['A','F']:
                print(response)
                response = input().upper()

            if response == 'A':
                playerhands[player]["bet"] = playerhands[player]["bet"] + playerhands[player]["balance"]
                playerhands[player]["balance"] = 0
                playerhands[player]["status"] = 1
            elif response == 'F':
                playerhands[player]["status"] = 3
    return playerhands



def deal_table(amount, deck, table=None):
    cards = deck[0:amount]
    del deck[0:amount]
    if table == None:
        return cards, deck
    else:
        for card in cards:
            table.append(card)
        return table, deck


def check_bet(playerhands):
    highestbet = get_highest_bet(playerhands)
    for player in playerhands:
        if playerhands[player]["status"] == 0:
            if True:
                pass



    


if __name__ == "__main__":
    # setup game
    deck = shuffle(config.gamedeck)
    playerhands = newtable()
    for player in playerhands:
        deck, playerhands = card_deal(playerhands, player, 2, deck)

    # players turn to add bets
    for player in playerhands:
        playerhands = add_bet(playerhands, player)
    
    # ensures players bet match
    for player in playerhands:
        playerhands = match_bet(playerhands, player)

    
    table, deck = deal_table(3, deck)
    
    


