import random

values = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]

class Deck:
    def __init__(self):
        self.cards = []
        self.deck()
        self.shuffle()

    def deck(self):
        for i in range(4):
            for j in values:
                self.cards.append(j)
    
    def print_deck(self):
        for card in self.cards:
            print(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop()

deck = Deck()
deck.print_deck()
deck.shuffle()

class Hand:
    def __init__(self):
        self.hand = []
        self.value = 0

    def add_card(self, card):
        self.hand.append(card)
        if card == "J" or card == "Q" or card == "K":
            self.value += 10
        elif card == "A":
            if self.value < 11:
                self.value += 11
            else:
                self.value += 1
        else:
            self.value += card

