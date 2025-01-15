import random
from blackjack_stick import play
import matplotlib.pyplot as plt

''' This is a bit of an experiment added because I've been interested in trying to make a genetic algorithm, 
had some extra time and thought I'd give it a go as an extension. As far 
as I can tell it hasn't worked very well, it is modelling the best score to stick on as around 14 which seems
too low. Either there is a problem in the rules of my initial game or (more likely) there's a problem with the
genetic algorithm. It's also completely untested, I hope you will forgive me for that! '''


population_size = 200
generations = 200
mutation_rate = 0.05

mean_stick_scores = []

#soft weight is a parameter that will make the stick score a bit higher if the hand has an ace, since an ace 
#can be one or eleven but is counted by the game as eleven where possible. A score is said to be 'soft' if it
#contains an ace, and 'hard' if not.
mean_soft_weights = []
best_win_rates = []

def fitness(stick_score):
    win_total = 0 
    for i in range(50):
        win_announcement = play(stick_score)
        if 'Dealer' in win_announcement:
            win_total += 0
        if 'Player_1' in win_announcement:
            win_total += 1
        else:
            win_total += 0

    win_rate = win_total/50
    return win_rate

def generate_population(size):
    return [[random.randint(1, 20), random.randint(0,5)] for i in range(size)]

# Selection should choose 200 new chromosomes from the best third of chromosomes based on fitness
def selection(population):
    sorted_population = sorted(population, key=fitness, reverse=True)
    return sorted_population[:len(population)//3]

# Crossbreed: The selection becomes the parents. They are crossbred by randomly taking one parameter from each parent.
def crossbreed(parent1, parent2):
    base_score = random.choice([parent1[0], parent2[0]])
    soft_weight = random.choice([parent1[1], parent2[1]])
    return [base_score, soft_weight]

# Mutation: Sometimes a childs parameters will be randomly mutated slightly 
import random

def mutate(stick_score):
    # Only a small percentage will be mutated
    if random.random() < mutation_rate:
        stick_score[0] += random.randint(-1, 1)
        stick_score[1] += random.uniform(-0.1, 0.1) 
        
        stick_score[0] = min(20, max(1, stick_score[0]))
        stick_score[1] = max(0, stick_score[1])

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
            # child = random.choice(parents)
            #Small chance to mutate the child
            child = mutate(child)
            #Add the child to the next generation
            next_generation.append(child)

        population = next_generation

        winning_stick_score = max(population, key=fitness)
        best_win_rate = fitness(winning_stick_score)
        best_win_rates.append(best_win_rate)

        mean_stick_score = round(sum([chrom[0] for chrom in population]) / population_size, 3)
        mean_stick_scores.append(mean_stick_score)

        mean_soft_weight = round(sum([chrom[1] for chrom in population])/ population_size, 3)
        mean_soft_weights.append(mean_soft_weight)

        print(f"Gen {generation} - mean stick score: {mean_stick_score}, mean soft weight: {mean_soft_weight}, best win rate: {best_win_rate}, winning stick score: {winning_stick_score}")

    
    return max(population, key=fitness)


if __name__ == '__main__':
    # print(fitness(17))
    best_score = genetic_algorithm()
    print(f"Best score to stick on: {best_score}")
    
    #Make a graph
    plt.figure(figsize=(10, 6))

    plt.plot(mean_stick_scores, label='Mean Stick Score', color='b')

    plt.plot(best_win_rates, label='Best Win Rate', color='g')

    plt.plot(mean_soft_weights, label='Mean Soft Weight (hands with aces)', color='r')

    plt.title('Blackjack Genetic Algorithm Over Generations')
    plt.xlabel('Generation')
    plt.ylabel('Value')
    plt.legend()
    plt.grid(True)
    plt.show()



  