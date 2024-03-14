from poly_sbst.crossover.abstract_crossover import AbstractCrossover
import numpy as np
from numpy import ndarray

class HTMLTestSuiteCrossover(AbstractCrossover):
    #child class of AbstractCrossover
    def __init__(self, cross_rate: float = 0.9):
        super().__init__(cross_rate)

    def _do_crossover(self, x:np.ndarray, y:np.ndarray) -> np.ndarray:
        #crossover the input by swapping a random segment of x with a random segment of y
        idx = np.random.randint(len(x))
        return np.concatenate((x[:idx], y[idx:]), axis=0)