# Python3 program to create target string, starting from
# random string using Genetic Algorithm

import random
import numpy
from PIL import Image

from Individual import *

# Number of individuals in each generation
POPULATION_SIZE = 200

# Generations limit
G_LIMIT = 100

# Valid genes
GENES = range(0, 255)

# Target is empty for now
TARGET = None

# Driver code
def main():
    global POPULATION_SIZE

    img = Image.open('jake.jpg')
    TARGET = numpy.array(img.getdata()).reshape(img.size[0], img.size[1], 3)

    # current generation
    generation = 1

    found = False
    population = []

    # create initial population
    for i in range(POPULATION_SIZE):
        Individual.set_genes(GENES)
        Individual.set_target(TARGET)
        gnome = Individual.create_gnome()
        population.append(Individual(gnome))
      

    while not found:

        # sort the population in increasing order of fitness score
        population = sorted(population, key=lambda x: x.fitness)

        # if the individual having lowest fitness score ie.
        # 0 then we know that we have reached to the target
        # and break the loop
        if population[0].fitness <= 0:
            found = True
            break

        # Otherwise generate new offsprings for new generation
        new_generation = []

        # Perform Elitism, that mean 10% of fittest population
        # goes to the next generation
        s = int((10 * POPULATION_SIZE) / 100)
        new_generation.extend(population[:s])

        # From 50% of fittest population, Individuals
        # will mate to produce offspring
        s = int((90 * POPULATION_SIZE) / 100)
        for _ in range(s):
            parent1 = random.choice(population[:50])
            parent2 = random.choice(population[:50])
            child = parent1.mate(parent2)
            new_generation.append(child)

        population = new_generation

        """print("Generation: {}\tString: {}\tFitness: {}". \
              format(generation,
                     "".join(population[0].chromosome),
                     population[0].fitness))
        """

        print("Generation: ", generation, " - fit: ", population[0].fitness)

        generation += 1
        if generation == G_LIMIT:
            break

    print("Generation: ", generation, " - fit: ", population[0].fitness)

    '''print("Generation: {}\tString: {}\tFitness: {}". \
        format(generation,
                "".join(population[0].chromosome),
                population[0].fitness))
    '''

    im = Image.fromarray(population[0].chromosome.astype('uint8')).convert('RGB')
    im.show()

if __name__ == '__main__':
    main()
