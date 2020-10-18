import random
import numpy


class Individual(object):
    '''
    Class representing individual in population
    '''

    def __init__(self, chromosome):
        self.chromosome = chromosome
        self.fitness = self.cal_fitness()
        self.genes = None
        self.target = None

    @classmethod
    def set_genes(self, genes):
        self.genes = genes

    @classmethod
    def set_target(self, target):
        self.target = target

    @classmethod
    def mutated_genes(self):
        '''
        create random genes for mutation
        '''
        r = random.choice(range(0, 255))
        g = random.choice(range(0, 255))
        b = random.choice(range(0, 255))
        return (r, g, b)

    @classmethod
    def create_gnome(self):
        '''
        create chromosome or string of genes
        '''
        pix = numpy.random.rand(100,100,3) * 255
        return pix

    # def mate(self, par2):
    #     '''
    #     Perform mating and produce new offspring
    #     '''
    #
    #     # chromosome for offspring
    #     child_chromosome = []
    #     for gp1, gp2 in zip(self.chromosome, par2.chromosome):
    #
    #         # random probability
    #         prob = random.random()
    #
    #         # if prob is less than 0.45, insert gene
    #         # from parent 1
    #         if prob < 0.45:
    #             child_chromosome.append(gp1)
    #
    #         # if prob is between 0.45 and 0.90, insert
    #         # gene from parent 2
    #         elif prob < 0.90:
    #             child_chromosome.append(gp2)
    #
    #         # otherwise insert random gene(mutate),
    #         # for maintaining diversity
    #         else:
    #             child_chromosome.append(self.mutated_genes())
    #
    #         # create new Individual(offspring) using
    #     # generated chromosome for offspring
    #     return Individual(child_chromosome)

    def mate(self, par2):
        '''
            Perform mating and produce new offspring
        '''
        # change 10 things at random
        child_chromosome = self.chromosome.copy()
        for i in range(10):
            idx = random.randint(0, 99)
            idy = random.randint(0, 99)
            r = random.choice(range(0, 255))
            g = random.choice(range(0, 255))
            b = random.choice(range(0, 255))
            child_chromosome[idx][idy] = (r, g, b)

        return Individual(child_chromosome)

    def cal_fitness(self):
        '''
        Calculate fittness score, it is the number of
        characters in string which differ from target
        string.
        '''
        fitness = 0
        for rows, rowt in zip(self.chromosome, self.target):
            for gs,gt in zip(rows, rowt):
                if int(gs[0]) != gt[0] and\
                        int(gs[1]) != gt[1] and\
                        int(gs[2]) != gt[2]:
                    fitness += 1
        return fitness
