import unittest
from src.game import Game
from src.player import Player, Dealer
        
class GameTestClass(unittest.TestCase):

    def setUp(self):
        self.test_player_1 = Player("Ruby")
        self.test_player_2 = Player("Ryan")
        self.test_player_3 = Player("Roland")
        self.game = Game(self.test_player_1, self.test_player_2, self.test_player_3)
        
        
    def tearDown(self):
        pass

    def test_game_cannot_have_less_than_one_player(self):
        with self.assertRaises(ValueError):
            Game()

    def test_game_can_shuffle_correctly(self):
        original_order = self.game.deck.cards.copy()
        self.game.shuffle()
        assert original_order!=self.game.deck.cards
    
    def test_game_can_deal_card_correctly(self):
        top_card = self.game.deck.cards[-1]
        drawn_card=self.game.deck.draw_card()
        assert top_card == drawn_card
    
    def test_game_deals_valid_card(self):
        self.assertIsInstance(self.game.deal_card(), str)
        self.assertIn('of', self.game.deal_card())
    
    def test_deal_inital_cards_deals_two_to_each_player(self):
        self.game.deal_initial_cards()
        
        self.assertEqual(len(self.game.players[0].hand), 2)
        self.assertEqual(len(self.game.players[1].hand), 2)
    
    def test_deal_initial_cards_deals_two_to_dealer(self):
        self.game.deal_initial_cards()
        assert len(self.game.dealer.hand) == 2
    
    def test_announce_winner_announces_winning_player_not21_correctly(self):
        test_card1 = 'Jack of spades'
        test_card2 = 'King of spades'
        test_card3 = '3 of clubs'
        test_card4 = '5 of hearts'
        test_card5 = '10 of spades'
        test_card6 = '9 of diamonds'
    
        self.test_player_1.receive_card(test_card1)
        self.test_player_1.receive_card(test_card2)
        self.test_player_2.receive_card(test_card3)
        self.test_player_2.receive_card(test_card4)
        self.game.dealer.receive_card(test_card5)
        self.game.dealer.receive_card(test_card6)

        self.assertEqual(self.game.announce_winner(), "Ruby wins with 20 points!")
    
    def test_announce_winner_announces_winning_dealer_pontoon_correctly(self):
        test_card1 = 'Ace of spades'
        test_card2 = 'King of spades'
        test_card3 = '3 of clubs'
        test_card4 = '5 of hearts'
        test_card5 = '10 of spades'
        test_card6 = '9 of diamonds'
    
        self.test_player_1.receive_card(test_card5)
        self.test_player_1.receive_card(test_card6)
        self.test_player_2.receive_card(test_card3)
        self.test_player_2.receive_card(test_card4)
        self.game.dealer.receive_card(test_card1)
        self.game.dealer.receive_card(test_card2)

        self.assertEqual(self.game.dealer.score, 21)
        self.assertEqual(self.game.announce_winner(), "Dealer wins with a pontoon worth 21 points.")
    
    def test_announce_winner_announces_winning_player_correctly_with_bust_hand(self):
        test_card1 = 'Ace of spades'
        test_card2 = 'King of spades'
        test_card3 = 'Jack of clubs'
        test_card4 = 'Jack of hearts'
        test_card5 = 'Jack of diamonds'
        test_card6 = '10 of spades'
        test_card7 = '9 of diamonds'
    
        self.test_player_1.receive_card(test_card1)
        self.test_player_1.receive_card(test_card2)
        self.test_player_2.receive_card(test_card3)
        self.test_player_2.receive_card(test_card4)
        self.test_player_2.receive_card(test_card5)
        self.game.dealer.receive_card(test_card6)
        self.game.dealer.receive_card(test_card7)

        self.assertEqual(self.game.announce_winner(), "Ruby wins with a pontoon worth 21 points!")
    
    def test_announce_winner_announces_correctly_all_bust(self):
        test_card1 = 'Queen of spades'
        test_card2 = 'King of spades'
        test_card3 = '5 of hearts'
        test_card4 = 'Jack of clubs'
        test_card5 = 'Jack of hearts'
        test_card6 = 'Jack of diamonds'
        test_card7 = '10 of spades'
        test_card8 = '9 of diamonds'
        test_card9 = '4 of clubs'
    
        self.test_player_1.receive_card(test_card1)
        self.test_player_1.receive_card(test_card2)
        self.test_player_1.receive_card(test_card3)
        self.test_player_2.receive_card(test_card3)
        self.test_player_2.receive_card(test_card4)
        self.test_player_2.receive_card(test_card5)
        self.game.dealer.receive_card(test_card6)
        self.game.dealer.receive_card(test_card7)
        self.game.dealer.receive_card(test_card8)

        self.assertEqual(self.game.announce_winner(), "All bust! Everybody loses...")

    def test_dealer_21_player_pontoon_announces_correctly(self):
        test_card1 = 'Ace of spades'
        test_card2 = 'King of spades'
        test_card3 = '9 of clubs'
        test_card4 = '4 of diamonds'
        test_card5 = '8 of hearts'
        self.test_player_1.receive_card(test_card1)
        self.test_player_1.receive_card(test_card2)
        self.game.dealer.receive_card(test_card3)
        self.game.dealer.receive_card(test_card4)
        self.game.dealer.receive_card(test_card5)
    
        self.assertEqual(self.game.announce_winner(), "Ruby wins with a pontoon worth 21 points!")
    
    def test_dealer_and_player_five_card_trick_announces_correctly(self):
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
        self.test_player_1.receive_card(test_card1)
        self.test_player_1.receive_card(test_card2)
        self.test_player_1.receive_card(test_card3)
        self.test_player_1.receive_card(test_card4)
        self.test_player_1.receive_card(test_card5)
        self.game.dealer.receive_card(test_card6)
        self.game.dealer.receive_card(test_card7)
        self.game.dealer.receive_card(test_card8)
        self.game.dealer.receive_card(test_card9)
        self.game.dealer.receive_card(test_card10)

        self.assertEqual(self.game.announce_winner(), "Dealer wins with a five card trick worth 21 points.")

    def test_dealer_bust_player_21_announces_correctly(self):
        test_card1 = 'Queen of hearts'
        test_card2 = 'King of spades'
        test_card3= '3 of clubs'
        test_card4 = 'Jack of spades'
        test_card5 = 'Ace of diamonds'
        self.game.dealer.receive_card(test_card1)
        self.game.dealer.receive_card(test_card2)
        self.game.dealer.receive_card(test_card3)
        self.test_player_1.receive_card(test_card4)
        self.test_player_1.receive_card(test_card5)

        self.assertEqual(self.game.announce_winner(), "Ruby wins with a pontoon worth 21 points!")
    
    def test_player_draw_dealer_bust(self):
        test_card1 = 'Queen of hearts'
        test_card2 = 'King of spades'
        test_card3= '3 of clubs'
        self.game.dealer.receive_card(test_card1)
        self.game.dealer.receive_card(test_card2)
        self.game.dealer.receive_card(test_card3)
        test_card4 = 'Jack of spades'
        test_card5 = 'Ace of diamonds'
        test_card6 = 'Jack of diamonds'
        test_card7 = 'Ace of spades'
        self.test_player_1.receive_card(test_card4)
        self.test_player_1.receive_card(test_card5)
        self.test_player_2.receive_card(test_card6)
        self.test_player_2.receive_card(test_card7)

        self.assertEqual(self.game.announce_winner(), "Ruby and Ryan draw with pontoons worth 21 points!")
    
    def test_player_draw_dealer_not_bust(self):
        test_card1 = 'Queen of hearts'
        test_card2= '8 of clubs'
        self.game.dealer.receive_card(test_card1)
        self.game.dealer.receive_card(test_card2)
        test_card3 = '10 of clubs'
        test_card4 = '9 of spades'
        
        test_card5 = 'Jack of diamonds'
        test_card6 = '9 of clubs'
        
        self.test_player_1.receive_card(test_card3)
        self.test_player_1.receive_card(test_card4)
        self.test_player_2.receive_card(test_card5)
        self.test_player_2.receive_card(test_card6)
        

        self.assertEqual(self.game.announce_winner(), "Ruby and Ryan draw with 19 points!")
    
    def test_three_player_draw_dealer_not_bust(self):
        

        test_card1 = 'Queen of hearts'
        test_card2= '8 of clubs'
        self.game.dealer.receive_card(test_card1)
        self.game.dealer.receive_card(test_card2)
        test_card3 = '10 of clubs'
        test_card4 = 'Jack of spades'
        test_card5 = 'Ace of diamonds'
        test_card6 = 'Jack of diamonds'
        test_card7 = '2 of spades'
        test_card8 = '9 of diamonds'
        test_card9 = 'Jack of hearts'
        test_card10 = '2 of clubs'
        test_card11 = '9 of hearts'
        self.test_player_1.receive_card(test_card3)
        self.test_player_1.receive_card(test_card4)
        self.test_player_1.receive_card(test_card5)
        self.test_player_2.receive_card(test_card6)
        self.test_player_2.receive_card(test_card7)
        self.test_player_2.receive_card(test_card8)
        self.test_player_3.receive_card(test_card9)
        self.test_player_3.receive_card(test_card10)
        self.test_player_3.receive_card(test_card11)

        self.assertEqual(self.game.announce_winner(), "Ruby, Ryan and Roland draw with 21 points!")
    
    def test_three_player_draw_five_card_trick_dealer_21(self):
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
        test_card18 =  '4 of spades'

        self.test_player_1.receive_card(test_card1)
        self.test_player_1.receive_card(test_card2)
        self.test_player_1.receive_card(test_card3)
        self.test_player_1.receive_card(test_card4)
        self.test_player_1.receive_card(test_card5)
        self.test_player_2.receive_card(test_card6)
        self.test_player_2.receive_card(test_card7)
        self.test_player_2.receive_card(test_card8)
        self.test_player_2.receive_card(test_card9)
        self.test_player_2.receive_card(test_card10)
        self.test_player_3.receive_card(test_card11)
        self.test_player_3.receive_card(test_card12)
        self.test_player_3.receive_card(test_card13)
        self.test_player_3.receive_card(test_card14)
        self.test_player_3.receive_card(test_card15)
        self.game.dealer.receive_card(test_card16)
        self.game.dealer.receive_card(test_card17)
        self.game.dealer.receive_card(test_card18)

        self.assertEqual(self.game.announce_winner(), "Ruby, Ryan and Roland draw with five card tricks worth 21 points!")
    


        




        











    
    



    
    






        

            