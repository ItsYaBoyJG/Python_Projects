import random

class GameCards:
    RANKS = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)

    SUITS = ('Spades', 'Hearts', 'Diamonds', 'Clubs')

    CARD_BACK = 'Deck/b.gif'


    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.file = "DECK/" +str(rank) + suit[0].lower() + "gif"
        self.faceUp = False


    def turn(self):
        self.faceUp = not self.faceUp
    
    def getFile(self):
        if self.faceUp:
            return self.file
        else:
            return GameCards.CARD_BACK
    
    def __str__(self):
        if self.rank == 1:
            rank = 'Ace'
        elif self.rank == 11:
            rank = 'Jack'
        elif self.rank == 12:
            rank = 'Queen'
        elif self.rank == 13:
            rank = 'King'
        else:
            rank = self.rank
        return str(rank) + 'of' + self.suit


class Deck(object):
    def __init__(self):
        self.cards = []
        for suit in GameCard.SUITS:
            for rank in GameCards.RANKS:
                c = Card(rank, suit)
                self.cards.append(c)

    def shuffle(self):
        random.shuffle(self.cards)
    
    def deal(self):
        if len(self) == 0:
            return None
        else: 
            return self.cards.pop(0)

    def cardsLeft(self):
        return len(self.cards)

    def __str__(self) -> str:
        self.result = ''
        for c in self.cards:
            self.result = self.result + str(c) + '\n'
        return self.result
