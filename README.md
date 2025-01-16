# Ruby Hirsch's Blackjack Game

My completed pre-assessment day task for the BBC Software Engineering Graduate Scheme 2025.

## Description

### Blackjack Rules

In Blackjack, players aim to get as close to 21 as possible without going over. Players can choose to "stick" (keep their current hand) or "twist" (draw another card) to improve their hand. The player with the best hand, greater than the dealer's but less than or equal to 21, wins. If there's a draw between a player and the dealer, the dealer wins. A "Pontoon" (a hand of Ace and a face card) beats a "Five Card Trick" (five cards that total 21), which beats a normal 21-point hand. If no one beats the dealer's hand, the dealer wins by default.

If a player is dealt two cards of the same rank, they can choose to 'split', moving the two cards into two separate hands that are each dealt two more cards. The player then plays each hand out in order. It is possible to split multiple times if one of the new hands is dealt another card of the same rank. 

### Multiplayer Pass and Play

The game can be played by up to eight players using a single device. If multiple players are involved, follow the in-game instructions to pass the device correctly between turns. All players should read the initial and closing messages, but during each player's turn, others should refrain from looking at the current player's screen while they make their move.

### Genetic Algorithm 

There is an attempt at a genetic algorithm which should model the best score threshold at which a player should stick in a game of blackjack against a dealer (dealer always twists until they bust or have a score of 17 or higher). It also tries to find the best value that should be added to the score threshold if the player's hand contains an ace (known as a soft score). 

Genetic algorithms are a technique inspired by natural selection. They create a population of potential solutions to a problem (referred to as chromosomes) and then iteratively improve them over 'generations'. Solutions are ranked based on their fitness and the best ones are selected to "reproduce" the next generation, which includes crossbreeding between 'parents' and a chance of mutation. In my very simplified version, this process takes place over 200 generations at which point an estimate is given for the best solution. 

## Getting Started

### Prerequisites

To run this program, make sure you have the following installed:

- **Python** (version 3.x)
- **Make** (if your system uses Makefile execution)

### Installing

1. Clone this repository to your local machine:

    ```
    git clone https://github.com/rmkbh/Blackjack-tech-test-rubyhirsch.git
    ```

2. Navigate to the project directory:

    ```
    cd Blackjack-tech-test-rubyhirsch
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

4. To run the genetic algorithm, and see a graph of the results, you can execute:

   ```
   python genetic_algorithm.py
   ```
