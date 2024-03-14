from poly_sbst.crossover.abstract_crossover import AbstractCrossover
import numpy as np
from numpy import ndarray

class UrlTestSuiteCrossover(AbstractCrossover):
    #child class of AbstractCrossover
    def __init__(self, cross_rate: float = 0.9):
        super().__init__(cross_rate)

    def _do_crossover(self, problem, a, b) -> tuple:
        #crossover the input by swapping a random segment of x with a random segment of y
        #for every link in a and b, swap a random segment of a with a random segment of b
        for i in range(min(len(a), len(b))):
            if np.random.rand() < self.cross_rate and len(a[i]) > 1 and len(b[i]) > 1:
                c = np.random.randint(0, len(a[i]))
                d = np.random.randint(0, len(b[i]))
                a[i] = a[i][:c] + b[i][d:]
                b[i] = b[i][:d] + a[i][c:]
        return a, b