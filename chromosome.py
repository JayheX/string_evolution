from math import floor
import random

class Chromosome:
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'Å', 'Ä', 'Ö', ' ', ',', '.']
    
    # The chromosome is initiated with a "gene code"
    def __init__(self, goal, code):
        self.code = code
        self.goal = goal

    def getGoal(self):
        return self.goal

    def countError(self):
        counter = 0
        error = 0
        for i in self.code:
            target = Chromosome.alphabet.index(self.goal[counter])
            value = Chromosome.alphabet.index(self.code[counter])
            error += (target - value)**2
            counter += 1
        return error

    def mate(self, other):
        length = len(self.code)
        r = random.randint(0, length - 1)
        pivot = floor(length/2)
        first = self.code[:pivot] + other.code[pivot:]
        second = other.code[:pivot] + self.code[pivot:]
        first = list(first)
        first[r] = random.choice(Chromosome.alphabet)
        first = "".join(first)
        second = list(second)
        second[r] = random.choice(Chromosome.alphabet)
        second = "".join(second)
        return Chromosome(self.goal, first), Chromosome(self.goal, second)
