import random

def read_input_file(filename):
    with open(filename) as f:
        n = int(f.readline().strip())
        transactions = []
        for i in range(n):
            op, amount = f.readline().strip().split()
            amount = int(amount)
            if op == 'l':
                transactions.append(amount)
            elif op == 'd':
                transactions.append(-amount)
        return transactions

def fitness_func(transactions, solution):
    balance = 0
    for i, t in enumerate(transactions):
        if solution[i]:
            balance += t
    return abs(balance)

def crossover_func(parent1, parent2):
    # Randomly choose crossover point
    crossover_point = random.randint(1, len(parent1) - 1)
    
    # Combine parents' solutions at the crossover point
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    
    return child1, child2

def mutate_func(solution, mutation_rate):
    for i in range(len(solution)):
        if random.random() < mutation_rate:
            solution[i] = not solution[i]
    return solution

def genetic_algorithm(transactions, pop_size, max_generations, mutation_rate):
    # Initialize population
    population = [[bool(random.getrandbits(1)) for _ in transactions] for _ in range(pop_size)]

    # Iterate for a fixed number of generations
    for generation in range(max_generations):
        # Evaluate fitness of each solution
        fitness_scores = [fitness_func(transactions, solution) for solution in population]

        # Check for a valid solution
        best_fitness = min(fitness_scores)
        if best_fitness == 0:
            best_index = fitness_scores.index(0)
            return population[best_index]

        # Select parents for crossover
        parent_indices = random.sample(range(pop_size), 2)
        parent1 = population[parent_indices[0]]
        parent2 = population[parent_indices[1]]

        # Apply crossover and mutation
        child1, child2 = crossover_func(parent1, parent2)
        child1 = mutate_func(child1, mutation_rate)
        child2 = mutate_func(child2, mutation_rate)

        # Replace least fit solution in population
        worst_index = fitness_scores.index(max(fitness_scores))
        if fitness_scores[worst_index] > fitness_func(transactions, child1):
            population[worst_index] = child1
        elif fitness_scores[worst_index] > fitness_func(transactions, child2):
            population[worst_index] = child2

    # Return best solution found
    return None

# Example usage
transactions = read_input_file("input.txt")
solution = genetic_algorithm(transactions, pop_size=100, max_generations=1000, mutation_rate=0.01)

if solution is not None and sum(solution) != 0:
    print(" ".join(str(int(x)) for x in solution))
else:
    print("-1")
