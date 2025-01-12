import unittest
from src.player import Participant, Player, Dealer
from src.game import Game
from src.deck import Deck

class PlayerTestCase(unittest.TestCase):

    def setUp(self):
        self.test_player = Player("Ruby")
        self.test_dealer = Dealer()
        self.test_game = Game(self.test_player)
        self.test_game.deck.shuffle()
    
    def tearDown(self):
        pass

    def test_player_name(self):
        assert self.test_player.name == "Ruby"

    def test_player_can_receive_one_card(self):
        test_card = "Queen of hearts"
        self.test_player.receive_card(test_card)
        assert self.test_player.hand == ["Queen of hearts"]
    
    def test_player_can_receive_multiple_cards(self):
        test_card1= "3 of clubs"
        test_card2= "6 of diamonds"
        self.test_player.receive_card(test_card1)
        self.test_player.receive_card(test_card2)
        assert self.test_player.hand==["3 of clubs", "6 of diamonds"]
    
    def test_receiving_cards_updates_score(self):
        test_card1= "3 of clubs"
        test_card2= "6 of diamonds"
        self.test_player.receive_card(test_card1)
        self.test_player.receive_card(test_card2)
        self.assertEqual(self.test_player.score, 9)

    def test_announce_returns_correct_for_two_cards(self):
        test_card1= "3 of clubs"
        test_card2= "6 of diamonds"
        self.test_player.receive_card(test_card1)
        self.test_player.receive_card(test_card2)
        assert self.test_player.announce_score() == 'Your hand scores 9 points.'
        assert self.test_player.score == 9

    def test_score_hand_returns_correct_for_hand_with_ace(self):
        test_card1 = "King of spades"
        test_card2 = "Ace of clubs"
        self.test_player.receive_card(test_card1)
        self.test_player.receive_card(test_card2)
        test_score = self.test_player.score
        
        self.assertEqual(self.test_player.announce_score(), 'Your hand scores 21 points.')
        self.assertEqual(test_score, 21)
    
    def test_score_hand_evaluates_correct_for_three_cards_one_ace(self):
        test_card1 = "King of spades"
        test_card2 = "Ace of clubs"
        test_card3 = "Queen of diamonds"
        self.test_player.receive_card(test_card1)
        self.test_player.receive_card(test_card2)
        self.test_player.receive_card(test_card3)
        test_score = self.test_player.score

        self.assertEqual(self.test_player.announce_score(),'Your hand scores 21 points.')
        self.assertEqual(test_score, 21)
    
    def test_score_hand_evaluates_correctly_multiple_aces(self):
        test_card1 = "Ace of spades"
        test_card2 = "Ace of clubs"
        test_card3 = "9 of diamonds"
        self.test_player.receive_card(test_card1)
        self.test_player.receive_card(test_card2)
        self.test_player.receive_card(test_card3)
        test_score = self.test_player.score

        self.assertEqual(self.test_player.announce_score(), 'Your hand scores 21 points.')
        self.assertEqual(test_score, 21)
    
    def test_score_returns_bust_for_bust_hand(self):
        test_card1 = "King of spades"
        test_card2 = "Jack of clubs"
        test_card3 = "9 of diamonds"
        self.test_player.receive_card(test_card1)
        self.test_player.receive_card(test_card2)
        self.test_player.receive_card(test_card3)
        test_score = self.test_player.score
        valid_hand = self.test_player.valid_hand

        self.assertEqual(self.test_player.announce_score(), 'Bust! Your hand scores 29 points.')
        self.assertEqual(test_score, 29)
        self.assertEqual(valid_hand, 0)
    
    def test_check_hand_valid_returns_bust_for_over_21(self):
        test_card1 = "King of spades"
        test_card2 = "Jack of clubs"
        test_card3 = "9 of diamonds"
        self.test_player.receive_card(test_card1)
        self.test_player.receive_card(test_card2)
        self.test_player.receive_card(test_card3)
        self.assertEqual(self.test_player.check_hand_valid(), 'Bust')
    
    def test_check_hand_valid_returns_valid_for_under_21(self):
        test_card1 = "King of spades"
        test_card2 = "Jack of clubs"
        self.test_player.receive_card(test_card1)
        self.test_player.receive_card(test_card2)
        
        self.assertEqual(self.test_player.check_hand_valid(), 'Valid')

    
    def test_twist_returns_string(self):
        self.test_game.deck = Deck() 
        self.test_game.deck.shuffle()
        test_card1 = "Jack of clubs"
        test_card2 = "9 of diamonds"
        self.test_player.receive_card(test_card1)
        self.test_player.receive_card(test_card2)
        
        self.assertIsInstance(self.test_player.twist(self.test_game), str) 
    
    def test_twist_fails_for_bust_hand(self):
        test_card1 = "King of spades"
        test_card2 = "Jack of clubs"
        test_card3 = "9 of diamonds"
        self.test_player.receive_card(test_card1)
        self.test_player.receive_card(test_card2)
        self.test_player.receive_card(test_card3)
        self.assertEqual(self.test_player.twist(self.test_game), 'Cannot twist on bust hand!')


    def test_twist_adds_card_to_hand(self):
        self.test_game.deck = Deck() 
        self.test_game.deck.shuffle()
        test_card1 = "Jack of clubs"
        test_card2 = "9 of diamonds"
        self.test_player.receive_card(test_card1)
        self.test_player.receive_card(test_card2)
        self.test_player.twist(self.test_game)
        self.assertEqual(len(self.test_player.hand), 3)
        
    
    def test_twist_changes_score_correctly(self):
        self.test_game.deck.cards = ['2 of clubs', '2 of diamonds']
        test_card1 = "3 of clubs"
        test_card2 = "9 of diamonds"
        self.test_player.receive_card(test_card1)
        self.test_player.receive_card(test_card2)
        self.test_player.twist(self.test_game)
        self.assertEqual(self.test_player.score, 14)

    def test_stick_returns_correct_string(self):
        test_card1 = "Jack of clubs"
        test_card2 = "9 of diamonds"
        self.test_player.receive_card(test_card1)
        self.test_player.receive_card(test_card2)
        self.assertEqual(self.test_player.stick(), "You stick with hand ['Jack of clubs', '9 of diamonds'] scoring 19 points.")
    
   
    
class DealerTestCase(unittest.TestCase):

    def setUp(self):
        self.test_dealer = Dealer()
        self.test_player = Player("Ruby")
        self.test_game = Game(self.test_player)
        self.test_game.deck = Deck()
        self.test_game.deck.shuffle()
        
    def tearDown(self):
        pass

    def test_dealer_name(self):
        self.assertEqual(self.test_dealer.name, "Dealer") 
    
     
    def test_twist_adds_card_to_dealer_hand(self):
        self.test_game.deck = Deck() 
        self.test_game.deck.shuffle()
        test_card1 = "Jack of clubs"
        test_card2 = "9 of diamonds"
        self.test_dealer.receive_card(test_card1)
        self.test_dealer.receive_card(test_card2)
        self.test_dealer.twist(self.test_game)
        self.assertEqual(len(self.test_dealer.hand), 3)

    def test_take_turn_keeps_drawing_cards_until_score_over_16(self):
        
        test_card1 = "Jack of clubs"
        test_card2 = "3 of diamonds"

        self.test_dealer.receive_card(test_card1)
        self.test_dealer.receive_card(test_card2)

        self.test_dealer.take_turn(self.test_game)

        self.assertGreaterEqual(self.test_dealer.score, 17)
    
    def test_take_turns_removes_card_from_the_deck_if_score_under_17(self):
        test_card1 = "Jack of clubs"
        test_card2 = "2 of diamonds"
        self.test_dealer.receive_card(test_card1)
        self.test_dealer.receive_card(test_card2)
        self.test_dealer.take_turn(self.test_game)
        self.assertLess(len(self.test_game.deck.cards), 52)
    
    def test_take_turn_sticks_if_score_higher_than_17(self):
        test_card1 = "Jack of clubs"
        test_card2 = "9 of diamonds"
        self.test_dealer.receive_card(test_card1)
        self.test_dealer.receive_card(test_card2)
        self.test_dealer.take_turn(self.test_game)
        self.assertEqual(len(self.test_game.deck.cards), 52)





        


        
if __name__ == '__main__':
    unittest.main()


        
        






     







        
'''Given I have a king and an ace
When my score is evaluated
Then my score is 21

Given I have a king, a queen, and an ace
When my score is evaluated
Then my score is 21

Given that I have a nine, an ace, and another ace
When my score is evaluated
Then my score is 21	'''





