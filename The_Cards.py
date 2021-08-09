

class Card:
    def __init__(self, suit, denomination, rank):
        self.suit = suit
        self.denomination = denomination
        self.rank = rank

    def show(self):
        print('{} of {} (rank # {})'.format(self.suit, self.denomination, self.rank))

class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    global ds
    ds = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    global rs
    rs = [1,2,3,4,5,6,7,8,9,10,11,12,13]

    def build(self):
        for d,r in zip(ds,rs):
            for s in ["Spades", "Clubs", "Diamonds", "Hearts"]:
                self.cards.append(Card(d,s,r))

    def show(self):
        for c in self.cards:
            c.show()

class Player:
    def __init__(self):
        pass

#
# card_1 = Card("Spades", "Ace", 13)
# card_1.show()
#
# d = ["Ace", "King", "Queen", "Jack", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
#
# d.reverse()
#
# print(d)

deck = Deck()
deck.show()

