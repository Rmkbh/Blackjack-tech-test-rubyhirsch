# Ruby Hirsch's Blackjack Game

My completed pre-assessment day task for the BBC Software Engineering Graduate Scheme 2025.

## Description

### Blackjack Rules

In Blackjack, players aim to get as close to 21 as possible without going over. Players can choose to "stick" (keep their current hand) or "twist" (draw another card) to improve their hand. The player with the best hand, greater than the dealer's but less than or equal to 21, wins. If there's a draw between a player and the dealer, the dealer wins. A "Pontoon" (a hand of Ace and a face card) beats a "Five Card Trick" (five cards that total 21), which beats a normal 21-point hand. If no one beats the dealer's hand, the dealer wins by default.

### Multiplayer Pass and Play

The game can be played by up to eight players using a single device. If multiple players are involved, follow the in-game instructions to pass the device correctly between turns. All players should read the initial and closing messages, but during each player's turn, others should refrain from looking at the current player's screen while they make their move.

## Getting Started

### Prerequisites

To run this program, make sure you have the following installed:

- **Python** (version 3.x)
- **Make** (if your system uses Makefile execution)

### Installing

1. Clone this repository to your local machine:

    ```
    git clone https://github.com/your-username/blackjack-game.git
    ```

2. Navigate to the project directory:

    ```
    cd blackjack-game
    ```

### Executing the Program

1. To run the program, execute the Makefile by running:

    ```
    make
    ```

2. Once the Makefile has run, you can start the Blackjack game by executing:

    ```
    python blackjack.py
    ```

3. Follow the on-screen instructions to play the game!
