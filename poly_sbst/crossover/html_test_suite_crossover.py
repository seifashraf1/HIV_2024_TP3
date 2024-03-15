from poly_sbst.crossover.abstract_crossover import AbstractCrossover
import numpy as np
from numpy import ndarray

class HTMLTestSuiteCrossover(AbstractCrossover):
    #child class of AbstractCrossover
    def __init__(self, cross_rate: float = 0.9):
        super().__init__(cross_rate)

    def _do_crossover(self, problem, a, b) -> tuple:
        #crossover the input by swapping a random segment of x with a random segment of y
        #for every link in a and b, divide a and b in half and swap the halves
        for i in range(max(len(a), len(b))):
            a_idx = np.random.randint(0, len(a))
            b_idx = np.random.randint(0, len(b))
            half_a = a[a_idx][len(a) // 2:]
            half_b = b[b_idx][len(b) // 2:]
            a[a_idx] = half_b + a[a_idx][:len(a) // 2]
            b[b_idx] = half_a + b[b_idx][:len(b) // 2]
        return a, b