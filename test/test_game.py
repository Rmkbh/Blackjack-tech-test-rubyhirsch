import pytest
from src.game import Game
from src.player import Player, Dealer

@pytest.fixture
def test_players():
    player1 = Player("Ruby")
    player2 = Player("Ryan")
    player3 = Player("Roland")
    return player1, player2, player3

@pytest.fixture
def game(test_players):
    player1, player2, player3 = test_players
    game = Game(player1, player2, player3)
    return game

# @pytest.fixture
# def player_pontoon(game):
#     player1, _, _ = test_players
#     test_card1 = 'Ace of spades'
#     test_card2 = 'King of spades'
#     player1.receive_card(test_card1)
#     player1.receive_card(test_card2)
#     return game

    
    


class TestGameInit:

    def test_game_cannot_have_less_than_one_player(self):
        with pytest.raises(ValueError):
            Game()
    
    def test_game_initializes_correctly(self, game):
        assert len(game.players) == 3
        assert isinstance(game.dealer, Dealer)

class TestShuffle:

    def test_game_can_shuffle_changes_order(self, game):
        original_order = game.deck.cards.copy()
        game.shuffle()
        assert original_order != game.deck.cards
    
    def test_shuffle_mantains_deck_length(self, game):
        game.shuffle()
        assert len(game.deck.cards) ==52

class TestDeal:

    def test_game_can_deal_card_correctly(self, game):
        top_card = game.deck.cards[-1]
        drawn_card = game.deck.draw_card()
        assert top_card == drawn_card

    def test_game_deals_valid_card(self, game):
        dealt_card = game.deal_card()
        assert isinstance(dealt_card, str)
        assert 'of' in dealt_card

    def test_deal_initial_cards_deals_two_to_each_player(self, game):
        game.deal_initial_cards()
        assert len(game.players[0].hands[0]) == 2
        assert len(game.players[1].hands[0]) == 2
        assert len(game.players[2].hands[0]) ==2

    def test_deal_initial_cards_deals_two_to_dealer(self, game):
        game.deal_initial_cards()
        assert len(game.dealer.hands[0]) == 2

class TestGameAnnouncements:

    def test_announce_winner_announces_winning_player_not21_correctly(self, game, test_players):
        player1, player2, _ = test_players
        test_card1 = 'Jack of spades'
        test_card2 = 'King of spades'
        test_card3 = '3 of clubs'
        test_card4 = '5 of hearts'
        test_card5 = '10 of spades'
        test_card6 = '9 of diamonds'

        player1.receive_card(test_card1)
        player1.receive_card(test_card2)
        player2.receive_card(test_card3)
        player2.receive_card(test_card4)
        game.dealer.receive_card(test_card5)
        game.dealer.receive_card(test_card6)

        assert game.announce_winner() == "Ruby wins with 20 points!"

    def test_announce_winner_announces_winning_dealer_pontoon_correctly(self, game, test_players):
        player1, player2, _ = test_players
        test_card1 = 'Ace of spades'
        test_card2 = 'King of spades'
        test_card3 = '3 of clubs'
        test_card4 = '5 of hearts'
        test_card5 = '10 of spades'
        test_card6 = '9 of diamonds'

        player1.receive_card(test_card5)
        player1.receive_card(test_card6)
        player2.receive_card(test_card3)
        player2.receive_card(test_card4)
        game.dealer.receive_card(test_card1)
        game.dealer.receive_card(test_card2)

        assert game.dealer.score[0] == 21
        assert game.announce_winner() == "Dealer wins with a pontoon worth 21 points."

    def test_announce_winner_announces_winning_player_correctly_with_bust_hand(self, game, test_players):
        player1, player2, _ = test_players
        test_card1 = 'Ace of spades'
        test_card2 = 'King of spades'
        test_card3 = 'Jack of clubs'
        test_card4 = 'Jack of hearts'
        test_card5 = 'Jack of diamonds'
        test_card6 = '10 of spades'
        test_card7 = '9 of diamonds'

        player1.receive_card(test_card1)
        player1.receive_card(test_card2)
        player2.receive_card(test_card3)
        player2.receive_card(test_card4)
        player2.receive_card(test_card5)
        game.dealer.receive_card(test_card6)
        game.dealer.receive_card(test_card7)

        assert game.announce_winner() == "Ruby wins with a pontoon worth 21 points!"

    def test_announce_winner_announces_correctly_all_bust(self, game, test_players):
        player1, player2, _ = test_players
        test_card1 = 'Queen of spades'
        test_card2 = 'King of spades'
        test_card3 = '5 of hearts'
        test_card4 = 'Jack of clubs'
        test_card5 = 'Jack of hearts'
        test_card6 = 'Jack of diamonds'
        test_card7 = '10 of spades'
        test_card8 = '9 of diamonds'
        
        player1.receive_card(test_card1)
        player1.receive_card(test_card2)
        player1.receive_card(test_card3)
        player2.receive_card(test_card3)
        player2.receive_card(test_card4)
        player2.receive_card(test_card5)
        game.dealer.receive_card(test_card6)
        game.dealer.receive_card(test_card7)
        game.dealer.receive_card(test_card8)

        assert game.announce_winner() == "All bust! Everybody loses..."

    def test_dealer_21_player_pontoon_announces_correctly(self, game, test_players):
        player1, _, _ = test_players
        test_card1 = 'Ace of spades'
        test_card2 = 'King of spades'
        test_card3 = '9 of clubs'
        test_card4 = '4 of diamonds'
        test_card5 = '8 of hearts'
        player1.receive_card(test_card1)
        player1.receive_card(test_card2)
        game.dealer.receive_card(test_card3)
        game.dealer.receive_card(test_card4)
        game.dealer.receive_card(test_card5)
    
        assert game.announce_winner() == "Ruby wins with a pontoon worth 21 points!"
    
    def test_dealer_and_player_five_card_trick_announces_correctly(self, game, test_players):
        player1, _, _ = test_players
        test_card1 = 'Ace of spades'
        test_card2 = '9 of spades'
        test_card3 = '2 of clubs'
        test_card4 = '4 of diamonds'
        test_card5 = '5 of hearts'
        test_card6 = 'Ace of hearts'
        test_card7 = '9 of hearts'
        test_card8 = '2 of diamonds'
        test_card9 = '4 of clubs'
        test_card10 = '5 of spades'
        player1.receive_card(test_card1)
        player1.receive_card(test_card2)
        player1.receive_card(test_card3)
        player1.receive_card(test_card4)
        player1.receive_card(test_card5)
        game.dealer.receive_card(test_card6)
        game.dealer.receive_card(test_card7)
        game.dealer.receive_card(test_card8)
        game.dealer.receive_card(test_card9)
        game.dealer.receive_card(test_card10)

        assert game.announce_winner() == "Dealer wins with a five card trick worth 21 points."

    def test_dealer_bust_player_21_announces_correctly(self, game, test_players):
        player1, _, _ = test_players  

        test_card1 = 'Queen of hearts'
        test_card2 = 'King of spades'
        test_card3 = '3 of clubs'
        test_card4 = 'Jack of spades'
        test_card5 = 'Ace of diamonds'
        
        game.dealer.receive_card(test_card1)
        game.dealer.receive_card(test_card2)
        game.dealer.receive_card(test_card3)
        player1.receive_card(test_card4)
        player1.receive_card(test_card5)

        assert game.announce_winner() == "Ruby wins with a pontoon worth 21 points!"
    
    def test_player_draw_dealer_bust(self, game, test_players):
        player1, player2, _ = test_players  

        test_card1 = 'Queen of hearts'
        test_card2 = 'King of spades'
        test_card3 = '3 of clubs'
        test_card4 = 'Jack of spades'
        test_card5 = 'Ace of diamonds'
        test_card6 = 'Jack of diamonds'
        test_card7 = 'Ace of spades'
        
        game.dealer.receive_card(test_card1)
        game.dealer.receive_card(test_card2)
        game.dealer.receive_card(test_card3)
        player1.receive_card(test_card4)
        player1.receive_card(test_card5)
        player2.receive_card(test_card6)
        player2.receive_card(test_card7)

        assert game.announce_winner() == "Ruby and Ryan draw with pontoons worth 21 points!"
    
    def test_player_draw_dealer_not_bust(self, game, test_players):
        player1, player2, _ = test_players  
        
        test_card1 = 'Queen of hearts'
        test_card2 = '8 of clubs'
        game.dealer.receive_card(test_card1)
        game.dealer.receive_card(test_card2)
        
        test_card3 = '10 of clubs'
        test_card4 = '9 of spades'
        test_card5 = 'Jack of diamonds'
        test_card6 = '9 of clubs'
        
        player1.receive_card(test_card3)
        player1.receive_card(test_card4)
        player2.receive_card(test_card5)
        player2.receive_card(test_card6)

        assert game.announce_winner() == "Ruby and Ryan draw with 19 points!"
    
    def test_three_player_draw_dealer_not_bust(self, game, test_players):
        player1, player2, player3 = test_players  
        
        test_card1 = 'Queen of hearts'
        test_card2 = '8 of clubs'
        game.dealer.receive_card(test_card1)
        game.dealer.receive_card(test_card2)
        
        test_card3 = '10 of clubs'
        test_card4 = 'Jack of spades'
        test_card5 = 'Ace of diamonds'
        test_card6 = 'Jack of diamonds'
        test_card7 = '2 of spades'
        test_card8 = '9 of diamonds'
        test_card9 = 'Jack of hearts'
        test_card10 = '2 of clubs'
        test_card11 = '9 of hearts'
        
        player1.receive_card(test_card3)
        player1.receive_card(test_card4)
        player1.receive_card(test_card5)
        player2.receive_card(test_card6)
        player2.receive_card(test_card7)
        player2.receive_card(test_card8)
        player3.receive_card(test_card9)
        player3.receive_card(test_card10)
        player3.receive_card(test_card11)

        assert game.announce_winner() == "Ruby, Ryan and Roland draw with 21 points!"
    
    def test_three_player_draw_five_card_trick_dealer_21(self, game, test_players):
        player1, player2, player3 = test_players  
        
       
        test_card1 = 'Ace of spades'
        test_card2 = '9 of spades'
        test_card3 = '2 of clubs'
        test_card4 = '4 of diamonds'
        test_card5 = '5 of hearts'
        test_card6 = 'Ace of hearts'
        test_card7 = '9 of hearts'
        test_card8 = '2 of diamonds'
        test_card9 = '4 of clubs'
        test_card10 = '5 of spades'
        test_card11 = 'Ace of clubs'
        test_card12 = '9 of clubs'
        test_card13 = '2 of spades'
        test_card14 = '4 of hearts'
        test_card15 = '5 of diamonds'
        test_card16 = '10 of hearts'
        test_card17 = '7 of hearts'
        test_card18 = '4 of spades'

        player1.receive_card(test_card1)
        player1.receive_card(test_card2)
        player1.receive_card(test_card3)
        player1.receive_card(test_card4)
        player1.receive_card(test_card5)
        player2.receive_card(test_card6)
        player2.receive_card(test_card7)
        player2.receive_card(test_card8)
        player2.receive_card(test_card9)
        player2.receive_card(test_card10)
        player3.receive_card(test_card11)
        player3.receive_card(test_card12)
        player3.receive_card(test_card13)
        player3.receive_card(test_card14)
        player3.receive_card(test_card15)
        game.dealer.receive_card(test_card16)
        game.dealer.receive_card(test_card17)
        game.dealer.receive_card(test_card18)

        assert game.announce_winner() == "Ruby, Ryan and Roland draw with five card tricks worth 21 points!"








    
    



    
    






        

            