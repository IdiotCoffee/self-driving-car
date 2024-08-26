import itertools
import random

class Evolution:
    def __init__(self, population_count, keep_count):
        self.population_count = population_count
        self.keep_count = keep_count

    def execute(self, rankable_chromosomes):
        #selection of best 4 parents, first sorted 
        sorted_chromosomes = [w.chromosome for w in sorted(rankable_chromosomes)]
        kept = sorted_chromosomes[:self.keep_count]


        #crossover
        iterations = (self.population_count - self.keep_count)/self.keep_count
        offspring = [c for c in kept]   #first copy best chromosomes to the offspring
        for _ in range(int(iterations)):
            for c1, c2 in itertools.batched(kept, 2):
                split_index = random.randint(0, len(c1) - 1)
                offspring.append(c1[:split_index]+c2[split_index:])
                offspring.append(c2[:split_index]+c1[split_index:])


        #mutation
        for chromosome in offspring[self.keep_count:]:
            for i in range(len(chromosome)):
                if random.randint(0, 4) == 1:
                    chromosome[i] = random.random() * 2 - 1

        assert len(offspring) == self.population_count, "offspring count is not population count"
        return offspring