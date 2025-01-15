import os
import platform
from src.game import Game
from src.player import Player

def initialise_game(player_names):
    players = []
    for name in player_names:
            players.append(Player(name))
    game = Game(*players)
    game.shuffle()
    game.deal_initial_cards()
    print(''' \n \n''')
    return game

def get_player_names():
    player_names = []
    player_count = 1

    while True:
        print(''' \n 
              ''')
        name = input(f'Player {player_count}, please enter your name:')
        if name.strip() == '':  
            print("Name cannot be empty. Please try again.")
            continue  
        
        while True:
            answer = input(f'Thanks {name}, are there any more players joining the game? Yes (y) or No (n):').lower()
            if answer not in ['y', 'yes', 'n', 'no']:
                print("Invalid input. Please try again.")
            else:
                break  

        if answer in ['y', 'yes']:
            player_names.append(name)
            player_count += 1
        else:
            player_names.append(name)
            break

    return player_names, player_count

def clear_console():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")