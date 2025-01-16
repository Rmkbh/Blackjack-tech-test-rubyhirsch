import pytest
from src.player import Player, Dealer
from src.game import Game
from src.deck import Deck

@pytest.fixture
def test_player():
    return Player("Ruby")

@pytest.fixture
def test_dealer():
    return Dealer()

@pytest.fixture
def test_game(test_player):
    game = Game(test_player)
    game.deck.shuffle()
    return game

class TestPlayer:
    def test_player_name(self, test_player):
        assert test_player.name == "Ruby"

    def test_player_can_receive_one_card(self, test_player):
        test_card = "Queen of hearts"
        test_player.receive_card(test_card)
        assert test_player.hands[0] == ["Queen of hearts"]

    def test_player_can_receive_multiple_cards(self, test_player):
        test_card1 = "3 of clubs"
        test_card2 = "6 of diamonds"
        test_player.receive_card(test_card1)
        test_player.receive_card(test_card2)
        assert test_player.hands[0] == ["3 of clubs", "6 of diamonds"]

    def test_receiving_cards_updates_score(self, test_player):
        test_card1 = "3 of clubs"
        test_card2 = "6 of diamonds"
        test_player.receive_card(test_card1)
        test_player.receive_card(test_card2)
        assert test_player.score[0] == 9

    def test_announce_returns_correct_for_two_cards(self, test_player):
        test_card1 = "3 of clubs"
        test_card2 = "6 of diamonds"
        test_player.receive_card(test_card1)
        test_player.receive_card(test_card2)
        assert test_player.announce_score() == 'Your hand scores 9 points.'
        assert test_player.score[0] == 9

    def test_score_hand_returns_correct_for_hand_with_ace(self, test_player):
        test_card1 = "King of spades"
        test_card2 = "Ace of clubs"
        test_player.receive_card(test_card1)
        test_player.receive_card(test_card2)
        assert test_player.announce_score() == 'Your hand scores 21 points.'
        assert test_player.score[0] == 21

    def test_twist_returns_string(self, test_player, test_game):
        test_game.deck = Deck()
        test_game.deck.shuffle()
        test_card1 = "Jack of clubs"
        test_card2 = "9 of diamonds"
        test_player.receive_card(test_card1)
        test_player.receive_card(test_card2)
        assert isinstance(test_player.twist(test_game), str)

    def test_twist_fails_for_bust_hand(self, test_player, test_game):
        test_card1 = "King of spades"
        test_card2 = "Jack of clubs"
        test_card3 = "9 of diamonds"
        test_player.receive_card(test_card1)
        test_player.receive_card(test_card2)
        test_player.receive_card(test_card3)
        assert test_player.twist(test_game) == 'Cannot twist on bust hand!'
    
    def test_split_raises_error_non_two_card_hand(self, test_player, test_game):
        with pytest.raises(ValueError):
            test_player.split(test_game) 
    
    def test_split_raises_error_different_rank_cards(self, test_player, test_game):
        test_player.receive_card("5 of hearts")
        test_player.receive_card("6 of clubs")
        with pytest.raises(ValueError):
            test_player.split(test_game)
    
    def test_split_adds_a_hand(self, test_player, test_game):
        test_player.receive_card("2 of diamonds")
        test_player.receive_card("2 of spades")
        test_player.split(test_game)
        assert len(test_player.hands) ==2
    
    def test_split_moves_second_card_to_new_hand(self, test_player, test_game):
        test_player.receive_card("2 of diamonds")
        test_player.receive_card("2 of spades")
        test_player.split(test_game)
        assert test_player.hands[1][0] == "2 of spades"
    
    def test_split_keeps_first_card_in_old_hand(self, test_player, test_game):
        test_player.receive_card("2 of diamonds")
        test_player.receive_card("2 of spades")
        test_player.split(test_game)
        assert test_player.hands[0][0] == "2 of diamonds"
    
    def test_split_deals_one_valid_card_to_each_split_hand(self, test_player, test_game):
        test_player.receive_card("2 of diamonds")
        test_player.receive_card("2 of spades")
        test_player.split(test_game)
        assert len(test_player.hands[0]) == 2
        assert len(test_player.hands[1]) == 2
        assert "of" in test_player.hands[0][1]
        assert "of" in test_player.hands[1][1]
    
    def test_split_can_split_again(self, test_player, test_game):
        test_player.receive_card("2 of diamonds")
        test_player.receive_card("4 of spades")
        test_player.hands.append(["2 of clubs", "2 of spades"])
        test_player.split(test_game, 1)
        assert len(test_player.hands) == 3
        assert len(test_player.hands[2]) == 2
    
    def test_can_split_returns_correct_non_two_card_hand(self, test_player): 
        assert test_player.can_split() == 'No'
    
    def test_can_split_returns_no_for_different_rank_cards(self, test_player):
        test_player.receive_card("5 of hearts")
        test_player.receive_card("6 of clubs")
        assert test_player.can_split() == 'No'
    
    def test_can_split_returns_yes_for_two_same_rank_cards(self, test_player):
        test_player.receive_card("5 of hearts")
        test_player.receive_card("5 of clubs")
        assert test_player.can_split() == 'Yes'
    
    def test_can_split_works_for_split_hands(self, test_player):
        test_player.receive_card("2 of diamonds")
        test_player.receive_card("4 of spades")
        test_player.hands.append(["2 of clubs", "2 of spades"])
        assert test_player.can_split(0) == 'No'
        assert test_player.can_split(1) == 'Yes'

class TestDealer:
    def test_dealer_name(self, test_dealer):
        assert test_dealer.name == "Dealer"

    def test_dealer_twist_adds_card_to_hand(self, test_dealer, test_game):
        test_game.deck.shuffle()
        test_card1 = "Jack of clubs"
        test_card2 = "9 of diamonds"
        test_dealer.receive_card(test_card1)
        test_dealer.receive_card(test_card2)
        test_dealer.twist(test_game)
        assert len(test_dealer.hands[0]) == 3

    def test_dealer_take_turn_keeps_drawing_until_score_over_16(self, test_dealer, test_game):
        test_card1 = "Jack of clubs"
        test_card2 = "3 of diamonds"
        test_dealer.receive_card(test_card1)
        test_dealer.receive_card(test_card2)
        test_dealer.take_turn(test_game)
        assert test_dealer.score[0] >= 17

    def test_dealer_take_turn_reduces_deck_count(self, test_dealer, test_game):
        test_card1 = "Jack of clubs"
        test_card2 = "2 of diamonds"
        test_dealer.receive_card(test_card1)
        test_dealer.receive_card(test_card2)
        test_dealer.take_turn(test_game)
        assert len(test_game.deck.cards) < 52

    def test_dealer_take_turn_sticks_if_score_higher_than_17(self, test_dealer, test_game):
        test_card1 = "Jack of clubs"
        test_card2 = "9 of diamonds"
        test_dealer.receive_card(test_card1)
        test_dealer.receive_card(test_card2)
        test_dealer.take_turn(test_game)
        assert len(test_game.deck.cards) == 52



        
        






     







        
'''Given I have a king and an ace
When my score is evaluated
Then my score is 21

Given I have a king, a queen, and an ace
When my score is evaluated
Then my score is 21

Given that I have a nine, an ace, and another ace
When my score is evaluated
Then my score is 21	'''





