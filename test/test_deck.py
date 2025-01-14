import pytest
from src.deck import Deck


@pytest.fixture
def test_deck():
    return Deck()

   
class TestDeck:

    def test_number_of_cards(self, test_deck):
        assert len(test_deck.cards) == 52

    def test_deck_has_13_each_suit(self, test_deck):
        suits = ["hearts", "diamonds", "clubs", "spades"]
        for suit in suits:
            assert sum(1 for card in test_deck.cards if suit in card) == 13

    def test_four_of_each_rank_in_deck(self, test_deck):
        ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
        for rank in ranks:
            assert sum(1 for card in test_deck.cards if rank in card) == 4

    def test_shuffle_changes_deck_order(self, test_deck):
        original_order = test_deck.cards.copy()
        test_deck.shuffle()
        assert original_order != test_deck.cards
        assert len(test_deck.cards) == 52

    def test_draw_card_returns_correct_card(self, test_deck):
        top_card = test_deck.cards[-1]
        drawn_card = test_deck.draw_card()
        assert top_card == drawn_card

    def test_draw_card_returns_valid_card(self, test_deck):
        drawn_card = test_deck.draw_card()
        assert isinstance(drawn_card, str)
        assert 'of' in drawn_card

    def test_draw_card_removes_correct_card_from_deck(self, test_deck):
        test_deck.shuffle()
        top_card = test_deck.cards[-1]
        test_deck.draw_card()
        assert top_card not in test_deck.cards
        assert len(test_deck.cards) == 51
        test_deck.draw_card()
        assert len(test_deck.cards) == 50
