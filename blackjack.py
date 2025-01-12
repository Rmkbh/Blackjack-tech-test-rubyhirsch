from src.deck import Deck
from src.player import Player, Dealer
from src.game import Game

def play():
    player_names = []
    player_count = 1
    print('''Welcome to BlackJack!
          ''')
    #I want an input to come up for a player to enter their name. I want that player saved as a player num 1 and so on, after each player has entered it should ask, any more players? If so it should ask again and save them as 2 etc
    
    while True:
        print(''' \n 
              ''')
        name = input(f'Player {player_count}, please enter your name:')
        if name.strip() == '':  
                print("Name cannot be empty. Please try again.")
        else:
            player_names.append(name)
        print(''' \n
              ''')
        answer = input(f'Thanks {name}, are there any more players joining the game? Yes (y) or No (n):').lower()
        if answer not in ['y', 'yes', 'n', 'no']:
             print("Invalid input. Please try again.")
        if answer == 'y' or answer== 'yes':
            player_count +=1
        else:
            break
    
    #Ok now I've got the players saved to players variable, I want to start a game. 
    while True:
        players = []
        for name in player_names:
            players.append(Player(name))
        game = Game(*players)
        game.shuffle()
        game.deal_initial_cards()
        num_of_players = game.num_of_players
        print(''' \n \n''')
        print(f'The dealer\'s upturned card is the {game.dealer.hand[0]}.')
        print(''' \n \n ''')

        for i in range(num_of_players):
            
            input(f'Please pass the device to {game.players[i].name} and enter "ok":')
            print(''' \n \n \n''')
            print(f'{game.players[i].name} you have been dealt: {game.players[i].hand} scoring {game.players[i].score} points.')
            
            while True:
                stick_twist_answer = input('Would you like to stick (s) or twist (t)?').lower()
                if stick_twist_answer == 't' or stick_twist_answer == 'twist':
                    print(game.players[i].twist(game))
                    if not game.players[i].valid_hand:
                        input('Enter "ok" to finish your turn:')
                        print('''\n \n \n \n \n \n \n \n \n \n \n \n \n \n''')
                        break
                
                elif stick_twist_answer not in ['s', 't', 'stick', 'twist']:
                    print('Invalid input. Please try again.')

                else:
                    print(game.players[i].stick())
                    input ('Enter "ok" to finish your turn:')
                    print('''\n \n \n \n \n \n \n \n \n \n \n \n \n 'n''')
                    break
        print('''\n \n \n \n \n \n \n \n \n \n''')
        print('The dealer will now take their turn...')
        print(f'The dealer\'s hand is {game.dealer.hand} scoring {game.dealer.score} points.')
        game.dealer.take_turn(game)
        print(''' \n ''')
        print(game.announce_winner())
        again = input("Another hand? Yes (y) or No (n)?:").lower()
        if again in ["yes", "y"]:
            pass
        else: 
            print("Thanks for playing Blackjack.")
            break




             







''' Things to improve: 1. need to refactor to account for draws. If there is a draw between a player and dealer the dealer wins (already coded), but if there is a draw between players it should be counted as a draw. DONE - now need to add in extra testing for draw cases. 
                       2. account for pontoons, ie a face card and an ace should beat any other forms of 21, next best is five card trick, then other 21s.
                       3. add in a split option. maybe work on chromosomal thing first..

'''
    

   




if __name__ == '__main__':
    play()
