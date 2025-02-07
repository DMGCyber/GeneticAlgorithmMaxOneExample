import random  # Importing Python's built-in random module for randomness

# ==========================
# PARAMETERS AND INITIALIZATION
# ==========================

GENE_POOL = [0, 1]  # The set of possible gene values (binary representation)
POP_SIZE = 6        # Number of individuals in the population
GENE_LENGTH = 10    # Length of each individual's chromosome (binary string)
MAX_GEN = 100       # Maximum number of generations the algorithm will run
PMUT = 0.1          # Probability of mutation per gene

# ==========================
# INITIALIZATION FUNCTION
# ==========================

def init_population():
    """
    Initializes a population of individuals.
    Each individual is represented as a list of binary values.
    
    Returns:
        A list of individuals, where each individual is a binary list of length GENE_LENGTH.
    """
    return [[random.choice(GENE_POOL) for _ in range(GENE_LENGTH)] for _ in range(POP_SIZE)]

# ==========================
# FITNESS FUNCTION
# ==========================

def fitness(individual):
    """
    Computes the fitness of an individual.
    In the MAXONE problem, fitness is simply the number of ones in the binary string.

    Args:
        individual (list): A binary list representing the individual.
    
    Returns:
        int: Number of ones in the individual's chromosome.
    """
    return sum(individual)

# ==========================
# SELECTION FUNCTION (Roulette Wheel Selection)
# Inspired by AIMA's select() function
# ==========================

def select(population):
    """
    Performs selection using a **Roulette Wheel Selection** method.
    Each individual's probability of being selected is proportional to its fitness.
    
    Args:
        population (list of lists): The current population of binary strings.
    
    Returns:
        list: A new selected population of the same size as the original population.
    """
    total_fitness = sum(fitness(ind) for ind in population)  # Compute total fitness of the population
    selection_probs = [fitness(ind) / total_fitness for ind in population]  # Probability distribution based on fitness
    selected = random.choices(population, weights=selection_probs, k=POP_SIZE)  # Select individuals using weighted sampling
    return selected

# ==========================
# CROSSOVER FUNCTION (Single-Point Crossover)
# Inspired by AIMA's recombine() function
# ==========================

def crossover(parent1, parent2):
    """
    Performs **single-point crossover** between two parents.
    
    Args:
        parent1 (list): First parent binary string.
        parent2 (list): Second parent binary string.
    
    Returns:
        tuple: Two offspring resulting from crossover.
    """
    if random.random() < 0.6:  # 60% chance to perform crossover
        point = random.randint(1, GENE_LENGTH - 1)  # Randomly select a crossover point (excluding 0)
        child1 = parent1[:point] + parent2[point:]  # First part from parent1, second from parent2
        child2 = parent2[:point] + parent1[point:]  # First part from parent2, second from parent1
        return child1, child2
    return parent1, parent2  # If no crossover occurs, return parents unchanged

# ==========================
# MUTATION FUNCTION
# Inspired by AIMA's mutate() function
# ==========================

def mutate(individual):
    """
    Applies **mutation** to an individual.
    Each gene in the chromosome has a probability `PMUT` of flipping.

    Args:
        individual (list): A binary list representing an individual.
    
    Returns:
        list: Mutated individual.
    """
    for i in range(len(individual)):
        if random.random() < PMUT:  # With probability PMUT, flip the bit
            individual[i] = 1 - individual[i]  # Flip 0 to 1 or 1 to 0
    return individual

# ==========================
# GENETIC ALGORITHM FUNCTION
# Inspired by AIMA's genetic_algorithm() function
# ==========================

def genetic_algorithm():
    """
    Implements the **Genetic Algorithm (GA)** for the MAXONE problem.
    
    Steps:
    1. Initialize a population of random individuals.
    2. Repeat for MAX_GEN generations:
       a. **Selection**: Choose individuals based on fitness.
       b. **Crossover**: Perform crossover on selected individuals.
       c. **Mutation**: Mutate some individuals.
       d. **Update**: Replace old population with new.
       e. **Check termination**: If an individual with max fitness (all 1s) is found, stop.
    """
    population = init_population()  # Step 1: Initialize population

    for generation in range(MAX_GEN):  # Step 2: Run for MAX_GEN generations
        selected_population = select(population)  # Step 2a: Selection

        # Step 2b: Crossover
        next_population = []
        for i in range(0, POP_SIZE, 2):
            child1, child2 = crossover(selected_population[i], selected_population[i+1])
            next_population.extend([child1, child2])

        # Step 2c: Mutation
        next_population = [mutate(ind) for ind in next_population]

        # Step 2d: Update population
        population = next_population

        # Step 2e: Track best individual
        best_individual = max(population, key=fitness)
        print(f"Generation {generation + 1}: Best Fitness = {fitness(best_individual)} | {best_individual}")

        # Step 2f: Termination condition (if solution is found)
        if fitness(best_individual) == GENE_LENGTH:
            print(f"Solution found in generation {generation + 1}: {best_individual}")
            break

# ==========================
# RUN THE GENETIC ALGORITHM
# ==========================

genetic_algorithm()  # Run the Genetic Algorithm for MAXONE
