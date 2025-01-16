class Participant:
    def __init__(self):
        self.name = 'default'
        self.hands = [[]]
        self.valid_hand = 1
        self.score = [0]
    
    def receive_card(self, card, hand_index=0):
        self.hands[hand_index].append(card)
        self.evaluate_score(hand_index)
           
    def evaluate_score(self, hand_index=0):
        if hand_index > (len(self.score)-1):
            self.score.insert(hand_index, 0)
        else:
            self.score[hand_index] = 0
        self.valid_hand = 1
        if len(self.hands[hand_index])>0:
            self.hands[hand_index] = [card for card in self.hands[hand_index] if card is not None]
            non_aces = [card for card in self.hands[hand_index] if ('Ace' not in card)]
            aces = [card for card in self.hands[hand_index] if ('Ace' in card)]

            for card in non_aces:
                
                rank_suit = card.split(" of ")
                
                if rank_suit[0] == 'King' or rank_suit[0] == 'Queen' or rank_suit[0] == 'Jack':
                    self.score[hand_index] +=10
                else:
                    self.score[hand_index] += int(rank_suit[0])

            for card in aces:
                if self.score[hand_index] + 11 > 21:
                    self.score[hand_index]+=1
                else:
                    self.score[hand_index]+=11
                
            if self.score[hand_index] > 1 and self.score[hand_index] <22:
                return self.score[hand_index]

            if self.score[hand_index] > 21:
                self.valid_hand -= 1
                return self.score[hand_index]
        else:
            return self.score[hand_index]
        
    def announce_score(self, hand_index=0):
        score = self.score[hand_index]
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
            raise ValueError("Valid hand checker faulty!")
        
    def twist(self, game, hand_index=0):
        
        if self.score[hand_index] > 21:
            return 'Cannot twist on bust hand!'
        if len(game.deck.cards)>0:
            card = game.deal_card()
            self.receive_card(card, hand_index)
            self.evaluate_score(hand_index)
            if self.name == 'Dealer':
                print(f'The dealer twists and receives the {card}. The dealer\'s hand is now {self.hands[hand_index]}.')
            else:
                print(f'You twist and receive the {card}. Your hand is now {self.hands[hand_index]}.')
            return self.announce_score(hand_index)
        else:
            raise ValueError("The deck has run out of cards!")
        
    def twist_alg(self, game, hand_index=0):
        
        if self.score[hand_index] > 21:
            return 'Cannot twist on bust hand!'
        if len(game.deck.cards)>0:
            card = game.deal_card()
            self.receive_card(card, hand_index)
            self.evaluate_score(hand_index)
            return self.announce_score(hand_index)
        else:
            raise ValueError("The deck has run out of cards!")
    
    def stick(self, hand_index=0):
        self.evaluate_score(hand_index)
        if self.name == 'Dealer':
            return f'The dealer sticks with hand {self.hands[hand_index]} scoring {self.score[hand_index]} points.'
        else:
            return f'You stick with hand {self.hands[hand_index]} scoring {self.score[hand_index]} points.'
    
    def stick_alg(self, hand_index=0):
        self.evaluate_score(hand_index)

    
class Player(Participant):

    def __init__(self, name):
        super().__init__()
        self.name = name
    
    def can_split(self, hand_index=0):
        if len(self.hands[hand_index]) ==2:
            if self.hands[hand_index][0].split(" of ")[0] == self.hands[hand_index][1].split(" of ")[0]:
                return 'Yes'
            else:
                return 'No'
        else: 
            return 'No'
         
    def split(self, game, hand_index=0):
        if len(self.hands[hand_index])==2:
            if self.hands[hand_index][0].split(" of ")[0] == self.hands[hand_index][1].split(" of ")[0]:
                #take the second card from first hand and move it into a second hand.
                second_card = self.hands[hand_index].pop()
                self.hands.append([second_card])
                #deal one new card to each of the split hands
                card1 = game.deal_card()
                self.receive_card(card1, hand_index)
                card2 = game.deal_card()
                self.receive_card(card2, len(self.hands)-1)
                return (f'You split and are dealt a {card1} and a {card2}. Your hands are now {self.hands}')
            else:
                raise ValueError("Splitting only allowed for two cards of the same rank.")
        else:   
            raise ValueError("Splitting only allowed with initial two cards.")


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
    
    def take_turn_alg(self, game):
        while self.evaluate_score() < 17:
            self.twist_alg(game)
        self.evaluate_score()
        if self.valid_hand:    
            self.stick_alg()



      
                
       


            
        
