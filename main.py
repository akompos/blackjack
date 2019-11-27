import random




class Card(object):
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val

    def show(self):
        return str(self.value) + str(self.suit)


class Deck(object):
    def __init__(self):
        self.cards = []
        self.__build()

    def __build(self):
        for suit in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for val in range(1,14):
                self.cards.append(Card(suit, val))

    def show(self):
        for card in self.cards:
            card.show()

    def shuffle(self):
        for i in range(len(self.cards)-1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cads[i]

    def drawCard(self):
        return self.cards.pop()


class Player(object):
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck):
        self.hand.append(deck.drawCard())
        return self

    def showhand(self):
        for card in self.hand:
            card.show()

    def discard(self):
        return self.hand.pop()

##card = Card("Clubs", 6)

#card.show()

#deck = Deck()
#print(len(deck.cards))
#deck.show()

#deck.shuffle()


#card = deck.drawCard()
#card.show()

alex = Player("Alex")
deck = Deck()
alex.draw(deck)
alex.showhand()

#dealer = Player("Dealer")
#dealer.draw(deck)
#dealer.showHand()

