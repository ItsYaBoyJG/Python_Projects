"""
A black jack game

currently only one player. PC is dealer

"""
import sys
import random
from matplotlib.pyplot import text
import numpy as np
import time
import colorsys
from tkinter import *
import Blackjack_Cards




class Player(object):
    def __init__(self, cards):
        self.cards = cards
        for cards in self.cards:
            cards.turn()

    def __str__(self):
		"""Returns string rep of cards and points."""
		result = ", ".join(map(str, self.cards))
		result += "\n  " + str(self.getPoints()) + " points"
		return result

	def hit(self, card):
		self.cards.append(card)
		
	def getPoints(self):
		count = 0
		for card in self._cards:
			if card.rank > 9:
				count += 10
			elif card.rank == 1:
				count += 11
			else:
				count += card.rank
		#Deduct 10 if Ace is available and need as 1
		for card in self._cards:
			if count <= 21:
				break
			elif card.rank == 1:
				count -= 10
		return count
		
	def hasBlackjack(self):
		"""Dealt 21 or not"""
		return len(self.cards) == 2 and self.getPoints() == 21
		
	def getCards(self):
		return self.cards

class Dealer(Player):
	"""Like a player, but with some restrictions"""
	
	def __init__(self, cards):
		"""Initial state: show one card only"""
		Player.__init__(self, cards)
		self.showOneCard = True
		self.cards[0].turn()
		
	def __str__(self):
		"""Return just one card if not hit yet."""
		if self._showOneCard:
			return str(self.cards[0])
		else:
			return Player.__str__(self)
			
	def hit(self, deck):
		"""Add cards while points < 17, then allow all to be shown."""
		while self.getPoints() < 17:
			card = deck.deal()
			card.turn()
			self._cards.append(card)
			
	def turnFirstCard(self):
		"""Turns over the first card to show it"""
		self.showOneCard = False
		self.cards[0].turn()

class Blackjack(object):
	
	def __init__(self):
		self.deck = Deck()
		self.deck.shuffle()
		
		#Pass the player and the dealer two cards each
		self.player = Player([self.deck.deal(), self.deck.deal()])
		self.dealer = Dealer([self.deck.deal(), self.deck.deal()])

	def getPlayerCards(self):
		"""Returns a list of the player's cards."""
		return self.player.getCards()
		
	def getDealerCards(self):
		"""Returns a list of the dealer's cards."""
		return self.dealer.getCards()
		
	def hitPlayer(self):
		"""Deals a card to the player. Returns a tuple of the card and the player's points."""
		card = self.deck.deal()
		card.turn()
		self.player.hit(card)
		return (card, self.player.getPoints())
		
	def hitDealer(self):
		"""Deals cards to the dealer until an outcome occurs. Returns a string representing the outcome."""
		self._dealer.turnFirstCard()
		playerPoints = self.player.getPoints()
		if playerPoints > 21:
			return "You bust and lose!"
		else:
			self.dealer.hit(self._deck)
			dealerPoints = self.dealer.getPoints()
			if dealerPoints > 21:
				return "Dealer busts, you win!"
			elif dealerPoints > playerPoints:
				return "Dealer wins :("
			elif dealerPoints < playerPoints and playerPoints <= 21:
				return "Congrats! You win!"
			elif dealerPoints == playerPoints:
				if self.player.hasBlackjack() and not self.dealer.hasBlackjack():
					return "Blackjack! You Win!"
				elif not self.player.hasBlackjack() and self.dealer.hasBlackjack():
					return "Dealer Blackjack! You lose!"
				else:
					return "There is a tie"

class GUI(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title("Blackjack")
        self.grid()


        #command buttons
        self.hitButton = Button(self, text= "Hit", command=self.hit)
        self.hitButton.grid(row=0,column=0)

        self.stayButton = Button(self, text= "Pass", command=self.stay)
        self.stayButton.grid(row=0, column=1)

        self.newGameButton = Button(self, text= "New Game", command=self.newGame)
        self.newGameButton.grid(row=0,column=2)


        #game status field
        self.status = StringVar
        self.statusField = Entry(self, textvariable=self.status)
        self.statusField.grid(row=1,column=0,columnspan=3)

        #game panes
        self.playerFrame = Frame(self)
        self.playerFrame.grid(row=2, column=0, columnspan=3)
        
        self.dealerFrame = Frame(self)
        self.dealerFrame.grid(row=3,column=0,columnspan=3)
        self.newGame()


    def newGame(self):
        self.model = Blackjack()

        # playercards 
        self.playerCardImages = list(map(lambda card: PhotoImage(file = card.getFilename()), self.model.getPlayerCards()))
        self.playerCardLabels = list(map(lambda x : Label(self.playerFrame, image = x), self.playerCardImages))
        for i in range(len(self.playerCardLabels)):
            self.playerCardLabels[i].grid(row=0,column=i)
        
        #dealer cards
        self.dealerCardImages = list(map(lambda card: PhotoImage(file = card.getFilename()), self.model.getDealerCards()))
        self.dealerCardLabels = list(map(lambda x : Label(self.dealerFrame, image= x), self.dealerCardImages))
        for i in range(len(self.dealerCardLabels)):
            self.dealerCardLabels[i].grid(row=0, column=i)
        
        # clear buttons and re enable them
        self.hitButton["state"] = NORMAL
        self.stayButton["state"] = NORMAL
        self.status.set("")

    
    def hit(self):
        (card, points) = self.model(Blackjack.hitPlayer())
        cardImage = PhotoImage(file = card.getFilename())
        self.playerCardImages.append(cardImage)
        label = Label(self.playerFrame, image= cardImage)
        self.playerCardLabels.append(label)
        label.grid(row=0, column=len(self.playerCardLabels) - 1)

        if points >= 21:
            self.roundPass()

    
    def roundPass(self):
        self.hitButton['state'] = DISABLED
        self.stayButton['state'] = DISABLED

        # hit dealer
        gameEnd = self.model.hitDealer()
        self.dealerCardImages = list(map(lambda card: PhotoImage(file = card.getFilename()), self.model.getDealerCards()))
        self.dealerCardLabels = list(map(lambda x : Label(self.dealerFrame, image= x), self.dealerCardImages))
        for i in range(len(self.dealerCardLabels)):
            self.dealerCardLabels[i].grid(row=0, column=i)
        self.status.set(gameEnd)

    

def main():
    GUI().mainloop()



if __name__ == "__main__":
    main()






