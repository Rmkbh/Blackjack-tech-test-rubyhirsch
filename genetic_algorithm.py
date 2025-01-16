import random
from blackjack_gen_alg import play
import matplotlib.pyplot as plt

''' This is a bit of an experiment added because I've been interested in trying to make a genetic algorithm, 
had some extra time and thought I'd give it a go as an extension. As far as I can tell it hasn't worked very well, 
it is modelling the best score to stick on as around 14 which seems too low. Either there is a problem in the rules
of my initial game or (more likely) there's a problem with the genetic algorithm. It's also completely un-unit-tested, 
although I have been thorougly trialling it by running it again and again and trying to make improvements. '''

population_size = 200
generations = 200
mutation_rate = 0.05

mean_stick_scores = []
#Soft weight is a parameter that will make the stick score a bit higher if the hand has an ace. A score is said to be 'soft' if it
#contains an ace, and 'hard' if not.
mean_soft_weights = []
#If the dealer has an ace they are likely to get a pontoon, so possibly makes the best stick threshold higher.
mean_dealer_ace_weights = []
best_win_rates = []

def fitness(stick_score):
    win_total = 0 
    for i in range(30):
        win_announcement = play(stick_score)
        if 'Dealer' in win_announcement:
            win_total += 0
        if 'Player_1' in win_announcement:
            win_total += 1
        else:
            win_total += 0.5

    win_rate = win_total/30
    return win_rate

def generate_population(size):
    return [[random.randint(1, 20), random.randint(0,5), random.randint(-1, 4)] for i in range(size)]

# Selection should choose 200 new chromosomes tournament style (selecting four random chromosomes and selecting the best one, 200 times)
def selection(population):
    selection = []
    for i in range(200):
        best_of_four_chromosomes = sorted(random.sample(population, 4), key=fitness, reverse=True)[0]
        selection.append(best_of_four_chromosomes)
    return selection

# Crossbreed takes two parents from the selection. We randomly select one of these parents to take each paramter (base score and soft weight) from.
def crossbreed(parent1, parent2):
    cut_length = random.randint(0, 3)
    child = parent1[:cut_length] + parent2[cut_length:]
    return child

# Mutation: 5% chance a child's parameters will be randomly mutated 
def mutate(stick_score):
   
    if random.random() < mutation_rate:
        stick_score[0] = random.randint(1, 20)
        stick_score[1] = random.randint(0, 5)
        stick_score[2] = random.randint(-1, 4)

    return stick_score  



# Genetic algorithm loop
def genetic_algorithm():
    population = generate_population(population_size)

    for generation in range(generations):
        
        # Select the fittest
        parents = selection(population)
        
        next_generation = []

        while len(next_generation) < population_size:
            #Take two random members of the last generation
            parent1, parent2 = random.sample(parents, 2)
            # Crossbreed them
            child = crossbreed(parent1, parent2)
            #Small chance to mutate the child
            child = mutate(child)
            #Add the child to the next generation
            next_generation.append(child)

        population = next_generation

        winning_stick_score = max(population, key=fitness)
        
        mean_stick_score = round(sum([chrom[0] for chrom in population]) / population_size, 3)
        mean_stick_scores.append(mean_stick_score)

        mean_soft_weight = round(sum([chrom[1] for chrom in population])/ population_size, 3)
        mean_soft_weights.append(mean_soft_weight)

        mean_dealer_ace_weight = round(sum([chrom[2] for chrom in population])/ population_size, 3)
        mean_dealer_ace_weights.append(mean_dealer_ace_weight)

        print(f"Gen {generation} - mean stick score: {mean_stick_score}, mean soft weight: {mean_soft_weight}, mean dealer ace weight: {mean_dealer_ace_weight}, winning stick score: {winning_stick_score}")

    
    return max(population, key=fitness)


if __name__ == '__main__':
    
    best_score = genetic_algorithm()
    print(f"Best score to stick on: {best_score}")
    
    #Make a graph
    plt.figure(figsize=(10, 6))

    plt.plot(mean_stick_scores, label='Mean Stick Score', color='b')

    plt.plot(mean_soft_weights, label='Mean Soft Weight (hands with aces)', color='r')

    plt.plot(mean_dealer_ace_weights, label= "Mean dealer upturned ace Weight", color = 'y')

    plt.title('Blackjack Genetic Algorithm Over Generations')
    plt.xlabel('Generation')
    plt.ylabel('Value')
    plt.legend()
    plt.grid(True)
    plt.show()



  