import pytest
from unittest.mock import patch
from blackjack import get_player_names, clear_console, initialise_game
from src.deck import Deck

@pytest.fixture
def test_game():
    test_player_names = ['Ruby', 'Ryan', 'Roland']
    test_game = initialise_game(test_player_names)
    return test_game

class TestInitialiseGame:
    
    def test_initialise_game_returns_correct_game(self, test_game):
    
        assert test_game.num_of_players == 3
        assert test_game.players[0].name == 'Ruby'
        assert test_game.players[1].name == 'Ryan'
        assert test_game.players[2].name == 'Roland'
    
    def test_deck_is_shuffled(self, test_game):
        unshuffled_deck = Deck()
        test_game_deck = test_game.deck

        assert unshuffled_deck != test_game_deck
    
    def test_initial_cards_dealt(self, test_game):
        player1hand = test_game.players[0].hands[0]
        player2hand = test_game.players[1].hands[0]
        player3hand = test_game.players[2].hands[0]

        assert len(player1hand) == len(player2hand) == len(player3hand) == 2


class TestGetPlayerNames:

    @patch('builtins.input', side_effect=['Ruby', 'n'])
    def test_get_player_names_single_player(self, mocked_input):
        player_names, player_count = get_player_names()
        assert player_names == ['Ruby']
        assert player_count == 1

    @patch('builtins.input', side_effect=['Ruby', 'y', 'Ryan', 'y', 'Roland', 'n'])
    def test_get_player_names_multiple_players(self, mocked_input):
        player_names, player_count = get_player_names()
        assert player_names == ['Ruby', 'Ryan', 'Roland']
        assert player_count == 3

    @patch('builtins.input', side_effect=['Ruby', 'j', 'y', 'Tuby', 'n'])
    def test_get_player_name_invalid_input_asks_again(self, mocked_input):
        player_names, player_count = get_player_names()
        assert player_names == ['Ruby', 'Tuby']
        assert player_count == 2

    @patch('builtins.input', side_effect=['', 'Ruby', 'y', '', 'Ryan', 'n'])
    def test_empty_name_asks_again(self, mocked_input):
        player_names, player_count = get_player_names()
        assert player_names == ['Ruby', 'Ryan']
        assert player_count == 2

class TestClearConsole:

    @patch("os.system")
    @patch("platform.system", return_value="Windows")
    def test_clear_console_calls_clear_windows(self, mock_platform, mock_system):
        clear_console()
        assert mock_system.call_count == 1

    @patch("os.system")
    @patch("platform.system", return_value="Linux")
    def test_clear_console_calls_clear_linux(self, mock_platform, mock_system):
        clear_console()
        assert mock_system.call_count == 1

    @patch("os.system")
    @patch("platform.system", return_value="Darwin")  
    def test_clear_console_calls_clear_macos(self, mock_platform, mock_system):
        clear_console()
        assert mock_system.call_count == 1

    

    

