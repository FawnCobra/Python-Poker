class players:
    def __init__(self, name: str, cards: list[str], status: int, balance: int, bet: int):
        self.name = name
        self.cards = cards
        self.status = status
        self.balance = balance
        self.bet = bet

    def __str__(self):
        return f"{self.name}:\n 'cards': {self.cards}, 'status': {self.status}, 'balance': {self.balance}, 'bet': {self.bet}"

testtable = {
    'player0': 
        {'cards': ['9,D', 'J,C'], 'status': 0, 'balance': 38, 'bet': 12}, 
    'player1': 
        {'cards': ['Q,C', '2,D'], 'status': 0, 'balance': 23, 'bet': 27}, 
    'player2': 
        {'cards': ['4,D', '3,D'], 'status': 0, 'balance': 0, 'bet': 50}
        }

p1 = players("player0", ['9,D', 'J,C'], 0, 38, 12)
p2 = players("player1",  ['Q,C', '2,D'], 0, 23, 27)
p3 = players("player2", ['4,D', '3,D'], 0, 0, 50)

testclasses = [p1, p2 , p3]

cardlen = 18

def display_table(playerhands):
    displaylist = ['','','','','','','','','']
    for player in playerhands:
        displaylist[0] = displaylist[0] + ("┏━━━━━━━━━━━━━━━━┓")
        displaylist[1] = displaylist[1] + (("┃" + player.center(cardlen - 2)  + "┃"))
        displaylist[2] = displaylist[2] + "┠────────────────┨"
        displaylist[3] = displaylist[3] + ("┃cards:          ┃")
        cards = str(playerhands[player]["cards"])
        displaylist[4] = displaylist[4] + (("┃" + cards.center(cardlen - 2) + "┃"))
        displaylist[5] = displaylist[5] + ("┃balance:" + str(playerhands[player]["balance"]).center(cardlen - 10) + "┃")
        displaylist[6] = displaylist[6] + ("┃bet:" + str(playerhands[player]["bet"]).center(cardlen - 6) + "┃")
        displaylist[7] = displaylist[7] + ("┃status:" + str(playerhands[player]["status"]).center(cardlen - 9) + "┃")
        displaylist[8] = displaylist[8] + "┗━━━━━━━━━━━━━━━━┛"

    for _ in displaylist:
        print(_)

def easy_readJSON(JSON):
    jsonstring = str(JSON)
    string = ''
    for _ in range(len(jsonstring)):
        if jsonstring[_] == '{':
            if len(string) == 0:
                string = string + jsonstring[_] + '\n'
            else:
                string = string + jsonstring[_] + '\n' + "    "
        elif jsonstring[_] == '}':
            try:
                if jsonstring[_ + 1] == ',':
                    string = string + jsonstring[_]
                if jsonstring[_ + 1] == '}':
                    string = string + jsonstring[_] + '\n'
            except IndexError:
                string = string + '   ' + jsonstring[_]
        elif jsonstring[_] == ',':
            if jsonstring[_ - 1] == '}':
                string = string + jsonstring[_] + '\n'
            else:
                string = string + jsonstring[_]
        else:
            string = string + jsonstring[_]
    return string


if __name__ == "__main__":
    # display_table(testtable)
    # print(easy_readJSON(testtable))
    totalbets = 0
    for _ in testclasses:
        print(_)
        totalbets += _.bet
        print(totalbets)
