from src.game import Game
from src.player import Player

#Simple automated version of the game where the player never splits, for genetic algorithm purposes

def initialise_game(player_names):
    players = []
    for name in player_names:
            players.append(Player(name))
    game = Game(*players)
    game.shuffle()
    game.deal_initial_cards()
    return game

def play(stick_score):
    
    player_names = ['Player_1']
    
    game = initialise_game(player_names)
    
    hand_index = 0
    player = game.players[0]
    
    while hand_index<len(player.hands):
        hand = player.hands[hand_index]

        #for most simple version, chromosomes choose not to split. could adapt this..
        while True:
            while player.can_split(hand_index) == 'Yes':
                split_answer = 'n'
                if split_answer in ['yes', 'y', 'split']:
                    player.split(game, hand_index)
                else:
                    break
            if 'Ace' in player.hands[0]:
                score = stick_score[0]+stick_score[1]
            else:
                score = stick_score[0]
            if player.score[0] >= score:
                stick_twist_answer = 's'
            else: 
                stick_twist_answer = 't'
            if stick_twist_answer == 't' or stick_twist_answer == 'twist':
                game.players[0].twist_alg(game, hand_index)
                if not game.players[0].valid_hand:
                    hand_index += 1
                    break
                else:
                    continue
                    
            else:
                game.players[0].stick_alg(hand_index)
                hand_index+=1
                break

    game.dealer.take_turn_alg(game)

    return game.announce_winner()





            
if __name__ == '__main__':
    stick_score = 17
    print(play(stick_score))
