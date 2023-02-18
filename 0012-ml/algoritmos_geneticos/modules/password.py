import random
from time import time


class GeneticPassword:

    def _generate(self, length, genes_set):
        genes = []
        while len(genes) < length:
            size = min(length - len(genes), len(genes_set))
            genes.extend(random.sample(genes_set, size))

        return ''.join(genes)


    def _mutate(self, parent, genes_set):
        index = random.randint(0, len(parent) -1)
        genes = list(parent)
        new_gene, alternate = random.sample(genes_set, 2)
        genes[index] = alternate if new_gene == genes[index] else new_gene

        return ''.join(genes)


    def getBest(
        self,
        fitness,
        target_len,
        optimal_fitness,
        genes_set,
        display
    ):
        random.seed()
        best_individual = self._generate(target_len, genes_set)
        best_fitness = fitness(best_individual)
        display(best_individual)

        if best_fitness > optimal_fitness:
            return best_individual
    
        while True:
            child = self._mutate(best_individual, genes_set)
            child_fitness = fitness(child)

            if best_fitness >= child_fitness:
                continue

            display(child)

            if child_fitness >= optimal_fitness:
                return child

            best_individual = child
            best_fitness = child_fitness


class TestGeneticPassword:
    def _fitness(self, genes):
        return sum(
            1 for expected, actual in zip(self.password, genes)
            if expected == actual
        )


    def _display(self, genes):
        fitness = self._fitness(genes)
        print(f'{genes} \t {fitness}')


    def getBest(self):
        t0 = time()
        result = GeneticPassword().getBest(
            self._fitness,
            len(self.password),
            len(self.password),
            self.genes,
            self._display
        )
        print(time() - t0)
        return result


    def __init__(self, password, genes):
        self.password = password
        self.genes = genes
