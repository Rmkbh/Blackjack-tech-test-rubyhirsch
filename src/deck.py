import random

class Deck:
    def __init__(self):
        card_stack = []
        for suit in ["hearts", "diamonds", "clubs", "spades"]:
            for i in range(1, 14):
                if i==1:
                    card_stack.append('Ace of '+ suit)
                if i>1 and i<11:
                    card_stack.append(str(i)+ ' of ' + suit)
                if i==11:
                    card_stack.append('Jack of ' + suit)
                if i==12:
                    card_stack.append('Queen of '+ suit)
                if i==13:
                    card_stack.append('King of '+suit)
        self.cards = card_stack

    def shuffle(self):
        random.shuffle(self.cards)
    
    def draw_card(self):
        if self.cards:
            return self.cards.pop()
        else:
            raise ValueError("The deck has run out of cards!")



