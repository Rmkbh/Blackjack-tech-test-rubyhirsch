from src.script_utils import get_player_names, clear_console, initialise_game
import time

def play():
    
    print('''Welcome to BlackJack!''')
    player_names_count = get_player_names()
    player_names = player_names_count[0]
    player_count = player_names_count[1]

    while True:
        
        number_of_busts = 0

        game = initialise_game(player_names)
       
        for i in range(player_count):
            hand_index = 0
            player = game.players[i]
            time.sleep(2)
            clear_console()
            input(f'Please pass the device to {player.name} and press "Enter":')
            print(''' \n \n \n''')

            while hand_index<len(player.hands):
                hand = player.hands[hand_index]
                print('\n \n')
                print(f'{player.name} you have been dealt: {hand} scoring {player.score[hand_index]} points. {number_of_busts} hands have bust. The dealer\'s upturned card is the {game.dealer.hands[0][0]}.')

                while True:
                    while player.can_split(hand_index) == 'Yes':
                        split_answer = input(f'Your hand is {hand} scoring {player.score[hand_index]} points. Would you like to split? Yes (y) or No (n):').lower()
                        if split_answer in ['yes', 'y', 'split']:
                            print(''' \n \n ''')
                            print(player.split(game, hand_index))
                            print(f'Your hand is: {player.hands[hand_index]} scoring {player.score[hand_index]} points. {number_of_busts} players have bust. The dealer\'s upturned card is the {game.dealer.hands[0][0]}.')

                        else:
                            break
  
                    stick_twist_answer = input('Would you like to stick (s) or twist (t)?').lower()
                    if stick_twist_answer == 't' or stick_twist_answer == 'twist':
                        print(''' \n \n ''')
                        print(game.players[i].twist(game, hand_index))
                        if not game.players[i].valid_hand:
                            number_of_busts +=1
                            hand_index += 1
                            break
                        else:
                            continue
                            
                    elif stick_twist_answer not in ['s', 't', 'stick', 'twist']:
                        print('Invalid input. Please try again.')
                        continue

                    else:
                        print(''' \n \n ''')
                        print(game.players[i].stick(hand_index))
                        hand_index+=1
                        break

            input('Please press "Enter" to finish your turn:')

        time.sleep(2)
        clear_console()

        print('The dealer will now take their turn...')
        print(f'The dealer\'s hand is {game.dealer.hands[0]} scoring {game.dealer.score[0]} points.')
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
