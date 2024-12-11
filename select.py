import random
from fit import *


def roulette_wheel_selection(population, fitness_scores):
    # Invert fitness to favor lower fitness values
    fitness_scores = inverted_fitness(fitness_scores)

    # Calculate total fitness (using inverted fitness values)
    total_fitness = sum(fitness_scores)

    # Calculate selection probabilities
    selection_probs = [fitness / total_fitness for fitness in fitness_scores]

    # Select individual based on the probabilities
    selected_index = random.choices(range(len(population)), weights=selection_probs, k=1)[0]

    return population[selected_index]


def tournament_selection(population, fitness_scores, tournament_size):
    # Select a random subset of individuals for the tournament
    tournament_indices = random.sample(range(len(population)), tournament_size)
    best = tournament_indices[0]

    for index in tournament_indices:
        if fitness_scores[index] < fitness_scores[best]:
            best = index


    return population[best]




def rank_selection(population, fitness_scores):
    ranked_indices = sorted(range(len(fitness_scores)), key=lambda i: fitness_scores[i])

    ranks = [rank + 1 for rank in range(len(fitness_scores))]  # Rank 1 is the best, rank N is the worst

    total_rank = sum(ranks)

    selection_probs = [rank / total_rank for rank in ranks]

    selected_index = random.choices(ranked_indices, weights=selection_probs, k=1)[0]

    # Return the selected individual
    return population[selected_index]

