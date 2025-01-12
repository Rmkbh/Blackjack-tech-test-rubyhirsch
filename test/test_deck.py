import unittest
from src.deck import Deck


class DeckTestCase(unittest.TestCase):

    def setUp(self):  # this method will be run before each test
        self.deck = Deck()

    def tearDown(self):  # this method will be run after each test
        pass

    def test_number_of_cards(self):  # any method beginning with 'test_' will be run by unittest
        number_of_cards = len(self.deck.cards)
        self.assertEqual(number_of_cards, 52)
    
    def test_deck_has_13_each_suit(self):
        number_of_hearts = 0
        number_of_diamonds = 0
        number_of_clubs = 0
        number_of_spades = 0

        for card in self.deck.cards:
            if 'hearts' in card:
                number_of_hearts+=1
            if 'diamonds' in card:
                number_of_diamonds+=1
            if 'clubs' in card:
                number_of_clubs+=1
            if 'spades' in card:
                number_of_spades+=1
            
        assert number_of_hearts==13
        assert number_of_diamonds==13
        assert number_of_clubs==13
        assert number_of_spades==13
    
    def test_four_of_each_rank_in_deck(self):
        ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        for rank in ranks:
            rank_in_deck_count = 0
            for card in self.deck.cards:
                if rank in card:
                    rank_in_deck_count+=1
            assert rank_in_deck_count == 4
    
    def test_shuffle_changes_deck_order(self):
        original_order = self.deck.cards.copy()
        self.deck.shuffle()
        assert original_order!=self.deck.cards
        self.assertEqual(len(self.deck.cards), 52)
        #There is a tiny chance that this test could wrongly fail, ie. if the cards are shuffled into the exact same order that they started in, but so minimal that this test is still practically fine.

    def test_draw_card_returns_correct_card(self):
        top_card = self.deck.cards[-1]
        drawn_card=self.deck.draw_card()
        assert top_card == drawn_card
    
    def test_draw_card_returns_valid_card(self):
        self.assertIsInstance(self.deck.draw_card(), str)
        self.assertIn('of', self.deck.draw_card())
    
    def test_draw_card_removes_correct_card_from_deck(self):
        self.deck.shuffle()
        top_card = self.deck.cards[-1]
        self.deck.draw_card()
        assert top_card not in self.deck.cards
        assert len(self.deck.cards)==51
        self.deck.draw_card()
        assert len(self.deck.cards)==50



    




if __name__ == '__main__':
    unittest.main()
