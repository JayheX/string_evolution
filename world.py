from chromosome import Chromosome
import random
from math import floor

class World:
    population = []
    generations = 0
    min_error = 1

    def __init__(self, code, chromosomes):
        self.code = code.upper()
        self.chromosomes = chromosomes

    def getCode(self):
        return self.code

    def getChromosomes(self):
        return self.chromosomes

    def populate(self):
        for i in range(0, self.getChromosomes()):
            c = ''.join(random.choice(Chromosome.alphabet) for x in range(0, len(self.code)))
            World.population.append(Chromosome(self.code, c))

    def addPopulation(seld, chromosome):
        World.population.append(chromosome)

    def getBest(self):
        print("At generation " + str(World.generations) + " the best candidate is " + str(World.population[0].code))

    def generation(self):
        pivot = floor(len(World.population)/2)
        World.population = sorted(World.population, key=lambda c: c.countError())[:pivot]
        World.min_error = World.population[0].countError()
        counter = 0
        stop = len(World.population)
        while counter < stop:
            members = World.population[counter].mate(World.population[counter + 1])
            for i in members:
                self.addPopulation(i)
            counter += 2
        World.generations += 1
