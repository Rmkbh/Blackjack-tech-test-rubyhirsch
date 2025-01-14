from src.player import Dealer
from src.deck import Deck

class Game:

    def __init__(self, *players):
        self.deck = Deck()
        if len(players)<1:
            raise ValueError("The game must have at least one player!")
        self.players = players
        self.num_of_players = len(players)
        self.dealer = Dealer()
        self.whose_turn = 1

    def shuffle(self):
        self.deck.shuffle()
    
    def deal_card(self):
        return self.deck.draw_card()
    
    def deal_initial_cards(self):
        for player in self.players:
            card1 = self.deal_card()
            player.receive_card(card1)
            card2 = self.deal_card()
            player.receive_card(card2)

        dealer_card1 = self.deal_card()
        dealer_card2 = self.deal_card()

        self.dealer.receive_card(dealer_card1)
        self.dealer.receive_card(dealer_card2)
    
    def announce_winner(self):
        highest_player_score = 0
        highest_scoring_player = None
        highest_scoring_player_hand = None
        for player in self.players:
            for i in range(len(player.score)):
                if player.score[i] > highest_player_score and player.score[i]<22:
                    highest_player_score = player.score[i]
                    highest_scoring_player = player
                    highest_scoring_player_hand = player.hands[i]

        #Non-21-dealer-win-case                
        if self.dealer.score[0] <21 and self.dealer.score[0] >= highest_player_score:
            return f"Dealer wins with {self.dealer.score[0]} points."
        
        #Non-21-dealer-lose-case
        elif (self.dealer.score[0]<21 and highest_player_score<21 and self.dealer.score[0]<highest_player_score) or (self.dealer.score[0]>21 and highest_player_score<21 and highest_player_score):
            winners = [highest_scoring_player.name]
            for player in self.players:
                for i in range(len(player.score)):
                    if player.name != highest_scoring_player.name:
                        if player.score[i] == highest_player_score and (player.name not in winners):
                            winners.append(player.name)
            if len(winners) ==1:
                return f"{highest_scoring_player.name} wins with {highest_player_score} points!"
            else:
                if len(winners) ==2:
                    return f"{winners[0]} and {winners[1]} draw with {highest_player_score} points!"
                else:
                    name_string = f'{winners[0]}'
                    for i in range(1, len(winners)-1):
                        name_string += f', {winners[i]}'
                    name_string += f' and {winners[-1]}'
                    return f'{name_string} draw with {highest_player_score} points!' 
            
        #21 points dealer cases 
        elif self.dealer.score[0] == 21 and self.dealer.score[0] > highest_player_score:
            if len(self.dealer.hands[0]) ==2:
                return f"Dealer wins with a pontoon worth {self.dealer.score[0]} points."
            elif len(self.dealer.hands[0]) == 5:
                return f"Dealer wins with a five card trick worth {self.dealer.score[0]} points."
            else: 
                return  "Dealer wins with 21 points."
        elif self.dealer.score[0] == 21 and self.dealer.score[0] == highest_player_score:
            if len(self.dealer.hands[0]) == 2:
                return f"Dealer wins with a pontoon worth {self.dealer.score[0]} points."
            
            elif len(self.dealer.hands[0]) !=2 and len(highest_scoring_player.hands[0]) ==2:
                
                pontoons = [highest_scoring_player]
                for player in self.players:
                    for i in range(len(player.score)):
                        if player != highest_scoring_player:
                            if player.score[i] == highest_player_score and len(player.hands[0])==2 and (player not in pontoons):
                                pontoons.append(player)
                if len(pontoons) ==1:
                    return f"{highest_scoring_player.name} wins with a pontoon worth 21 points!"
                elif len(pontoons) ==2:
                    return f"{pontoons[0].name} and {pontoons[1].name} draw with pontoons worth 21 points!"
                else:
                    name_string = f'{pontoons[0].name}'
                    for i in range(1, len(pontoons)-1):
                        name_string += f', {pontoons[i].name}'
                    name_string += f' and {pontoons[-1].name}'
                    return f'{name_string} draw with pontoons worth 21 points!'
            

            elif len(self.dealer.hands[0]) == 5:
                return f"Dealer wins with a five card trick worth 21 points."
            
            elif len(self.dealer.hands[0]) !=5 and len(highest_scoring_player.hands[0]) == 5:
                five_card_tricks = [highest_scoring_player]
                for player in self.players:
                    for i in range(len(player.score)):
                        if player != highest_scoring_player:
                            if player.score[i] == highest_player_score and len(player.hands[0])==5 and (player not in five_card_tricks):
                                five_card_tricks.append(player)

                if len(five_card_tricks) ==1:
                    return f"{highest_scoring_player.name} wins with a five card trick worth {highest_player_score} points!"
                elif len(five_card_tricks) ==2:
                    return f"{five_card_tricks[0].name} and {five_card_tricks[1].name} draw with five card tricks worth 21 points!"
                else:
                    name_string = f'{five_card_tricks[0].name}'
                    for i in range(1, len(five_card_tricks)-1):
                        name_string += f', {five_card_tricks[i].name}'
                    name_string += f' and {five_card_tricks[-1].name}'
                    return f'{name_string} draw with five card tricks worth 21 points!'
            
        #21 points player cases
        elif (self.dealer.score[0] <21 or self.dealer.score[0]>21) and highest_player_score == 21:
            winners = [highest_scoring_player]
            for player in self.players:
                for i in range(len(player.score)):
                    if player != highest_scoring_player:
                        if player.score[i] == highest_player_score and (player not in winners):
                            winners.append(player)
            if len(winners) == 1:
                if len(highest_scoring_player.hands[0])==2:
                    return f"{highest_scoring_player.name} wins with a pontoon worth 21 points!"
                elif len(highest_scoring_player.hands[0]) == 5:
                    return f"{highest_scoring_player.name} wins with a five card trick worth 21 points!"
                else:
                    return f"{highest_scoring_player.name} wins with 21 points!"
            else:
                pontoons = []
                five_card_tricks = []
                neither = []
                for winner in winners:
                    if len(winner.hands[0]) == 2:
                        pontoons.append(winner)
                    elif len(winner.hands[0]) == 5:
                        five_card_tricks.append(winner)
                    else:
                        neither.append(winner)
                if len(pontoons)>0:
                    if len(pontoons)==1:
                        return f'{pontoons[0].name} wins with a pontoon worth 21 points!'
                    elif len(pontoons) == 2:
                        return f'{pontoons[0].name} and {pontoons[1].name} draw with pontoons worth 21 points!'
                    else:
                        name_string = f'{pontoons[0].name}'
                        for i in range(1, len(pontoons)-1):
                            name_string += f', {pontoons[i].name}'
                        name_string += f' and {pontoons[-1].name}'
                        return f'{name_string} draw with pontoons worth 21 points!'
                elif len(five_card_tricks)>0:
                    if len(five_card_tricks)==1:
                        return f'{five_card_tricks[0].name} wins with a five card trick worth 21 points!'
                    elif len(five_card_tricks) == 2:
                        return f'{five_card_tricks[0].name} and {five_card_tricks[1].name} draw with five card tricks worth 21 points!'
                    else:
                        name_string = f'{five_card_tricks[0].name}'
                        for i in range(1, len(five_card_tricks)-1):
                            name_string += f', {five_card_tricks[i].name}'
                        name_string += f' and {five_card_tricks[-1].name}'
                        return f'{name_string} draw with five card tricks worth 21 points!'
                elif len(neither) > 0:
                    if len(neither)==1:
                        return f'{neither[0].name} wins with 21 points!'
                    elif len(neither) == 2:
                        return f'{neither[0].name} and {neither[1].name} draw with 21 points!'
                    else:
                        name_string = f'{neither[0].name}'
                        for i in range(1, len(neither)-1):
                            name_string += f', {neither[i].name}'
                        name_string += f' and {neither[-1].name}'
                        return f'{name_string} draw with 21 points!'

        else:
            return "All bust! Everybody loses..."




    

            


        

        
    


        
        

        

                
        
        

        
