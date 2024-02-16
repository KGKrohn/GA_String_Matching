import numpy as np
import random
import string


num_pop = 2000
num_genes = 50
mutation_rate = 0.04
TARGET = "KRISTIAN_KROHN*581816"
TARGET = TARGET.upper()
caracters = string.ascii_letters.upper() + string.punctuation + string.digits


def create_genes(): # create a random character
    smol = random.choice(caracters)
    return smol


def create_crom(): # Creat an array random character
    empty_population = []
    for i in range(len(TARGET)):
        empty_population.append(create_genes())
    return empty_population


def crossover(parent1, parent2): # Uniform crossover implementation
    crossover_point = random.randint(0, len(parent1) - 1)
    child1 = np.concatenate((parent1[:crossover_point], parent2[crossover_point:]))
    child2 = np.concatenate((parent2[:crossover_point], parent1[crossover_point:]))
    return child1, child2


def mutation(child): # if the random number is lower then the mutation_rate the gene in the cromosone will be randomized
    mutated_child = child.copy()
    for i in range(len(mutated_child)):
        if random.random() < mutation_rate:
            mutated_child[i] = create_genes()
    return mutated_child


def create_offspring(population, pop_nr): # define the parents form a sorted list and pick a random form the top 10
    new_generation = []
    while len(new_generation) < len(pop_nr):
        parent1 = random.choice(population[:10])
        parent2 = random.choice(population[:10])
        child1, child2 = crossover(parent1, parent2)
        child1 = mutation(child1)
        child2 = mutation(child2)
        new_generation.append(child1)
        new_generation.append(child2)
    return new_generation


def cal_fitness(guess): # for each wrong gene in the array add 1 to fitness for the cromoson
    global TARGET
    fitness = 0
    for gs, gt in zip(guess, TARGET):
        if gs != gt:
            fitness += 1
    return fitness


def sort_strings_by_fitness(list_of_lists): # Sort the list based on the fitnes form the lowest fitnes to the highest.
    return sorted(list_of_lists, key=lambda x: cal_fitness(x))
