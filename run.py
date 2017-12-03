from world import World
from chromosome import Chromosome

w = World("jos tähän nyt vaan laittaa randomilla jotain sanoja vitun paljon peräkkäin niin että tästä tulee tosi pitkä", 20)
w.populate()
while w.min_error != 0:
    #print("At generation " + str(w.generations) + " the best candidate is " + str(w.population[0].code))
    w.generation()
print("It took us a whopping " + str(w.generations) + " generations.")