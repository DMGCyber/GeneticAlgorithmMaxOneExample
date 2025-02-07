import random

# Define parameters
GENE_POOL = [0, 1]  # Binary values
POP_SIZE = 6        # Number of individuals
GENE_LENGTH = 10    # Length of binary string
MAX_GEN = 100       # Maximum generations
PMUT = 0.1          # Mutation probability

# Initialize population
def init_population():
    return [[random.choice(GENE_POOL) for _ in range(GENE_LENGTH)] for _ in range(POP_SIZE)]

# Fitness function: Count the number of ones
def fitness(individual):
    return sum(individual)

# Selection: Roulette Wheel Selection
def select(population):
    total_fitness = sum(fitness(ind) for ind in population)
    selection_probs = [fitness(ind) / total_fitness for ind in population]
    selected = random.choices(population, weights=selection_probs, k=POP_SIZE)
    return selected

# Crossover: Single-point crossover
def crossover(parent1, parent2):
    if random.random() < 0.6:  # 60% chance of crossover
        point = random.randint(1, GENE_LENGTH - 1)
        child1 = parent1[:point] + parent2[point:]
        child2 = parent2[:point] + parent1[point:]
        return child1, child2
    return parent1, parent2  # No crossover, return unchanged

# Mutation: Flip a random bit with probability PMUT
def mutate(individual):
    for i in range(len(individual)):
        if random.random() < PMUT:
            individual[i] = 1 - individual[i]  # Flip bit
    return individual

# Genetic Algorithm
def genetic_algorithm():
    population = init_population()
    for generation in range(MAX_GEN):
        # Selection
        selected_population = select(population)

        # Crossover
        next_population = []
        for i in range(0, POP_SIZE, 2):
            child1, child2 = crossover(selected_population[i], selected_population[i+1])
            next_population.extend([child1, child2])

        # Mutation
        next_population = [mutate(ind) for ind in next_population]

        # Update population
        population = next_population

        # Best individual so far
        best_individual = max(population, key=fitness)
        print(f"Generation {generation + 1}: Best Fitness = {fitness(best_individual)} | {best_individual}")

        # Termination Condition: If we reach max ones
        if fitness(best_individual) == GENE_LENGTH:
            print(f"Solution found in generation {generation + 1}: {best_individual}")
            break

# Run the genetic algorithm
genetic_algorithm()
