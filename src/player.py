class Participant:
    def __init__(self):
        self.name = 'default'
        self.hand = []
        self.valid_hand = 1
        self.score = 0
    
    def receive_card(self, card):
        self.hand.append(card)
        self.evaluate_score()
           
    def evaluate_score(self):
        self.score = 0
        self.valid_hand = 1
        if len(self.hand)>0:
            self.hand = [card for card in self.hand if card is not None]
            non_aces = [card for card in self.hand if ('Ace' not in card)]
            aces = [card for card in self.hand if ('Ace' in card)]

            

            for card in non_aces:
                
                rank_suit = card.split(" of ")
                
                if rank_suit[0] == 'King' or rank_suit[0] == 'Queen' or rank_suit[0] == 'Jack':
                    self.score +=10
                else:
                    self.score += int(rank_suit[0])

            for card in aces:
                if self.score + 11 > 21:
                    self.score+=1
                else:
                    self.score+=11
                
            if self.score > 1 and self.score <22:
                return self.score

            if self.score > 21:
                self.valid_hand -= 1
                return self.score
        else:
            return self.score
        
    def announce_score(self):
        score = self.score
        if score < 22:
            if self.name == 'Dealer':
                return f"The dealer's hand scores {score} points."
            else:
                return f"Your hand scores {score} points."
        if score > 21:
            if self.name == 'Dealer':
                return f"Bust! The dealer's hand scores {score} points."
            else:
                return f"Bust! Your hand scores {score} points."
    
    def check_hand_valid(self):
        if self.valid_hand == 1:
            return 'Valid'
        elif self.valid_hand == 0:
            return 'Bust'
        else:
            return 'Error with valid hand checker'
        
    
    def twist(self, game):
        
        if self.score > 21:
            return 'Cannot twist on bust hand!'
        if len(game.deck.cards)>0:
            card = game.deal_card()
            self.receive_card(card)
            self.evaluate_score()
            if self.name == 'Dealer':
                print(f'The dealer twists and receives the {card}. The dealer\'s hand is now {self.hand}.')
            else:
                print(f'You twist and receive the {card}. Your hand is now {self.hand}.')
            return self.announce_score()
        else:
            raise ValueError("The deck has run out of cards!")
    
    def stick(self):
        self.evaluate_score()
        if self.name == 'Dealer':
            return f'The dealer sticks with hand {self.hand} scoring {self.score} points.'
        else:
            return f'You stick with hand {self.hand} scoring {self.score} points.'


class Player(Participant):

    def __init__(self, name):
        super().__init__()
        self.name = name
        
        
    
class Dealer(Participant):
    def __init__(self):
        super().__init__()
        self.name = "Dealer"
             
    
       
    def take_turn(self, game):
        
        while self.evaluate_score() < 17:
            print(self.twist(game))
        self.evaluate_score()
        if self.valid_hand:    
            print(self.stick())


      
                
       


            
        
