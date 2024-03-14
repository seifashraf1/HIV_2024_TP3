from poly_sbst.mutation.abstract_mutation import AbstractMutation
import numpy as np
import random
import copy

class HTMLTestSuiteMutation(AbstractMutation):
    '''
    Class for mutation of HTML test suites
    '''
    def __init__(self, mut_rate: float = 0.4, generator=None):
        super().__init__(mut_rate, generator)

    def _do_mutation(self, x) -> np.ndarray:

        possible_mutations = [
            self._delete_random_character,
            self._insert_random_character,
            self._replace_random_character
        ]
        mutator = np.random.choice(possible_mutations)

        return mutator(x)

    def _delete_random_character(self, s):
        """Returns s with a random character deleted"""
        for url in s:
            if len(url) > 5:
                pos = random.randint(0, len(url) - 1)
                url = url[:pos] + url[pos + 1 :]
        return s

    def _insert_random_character(self, s):
        """Returns s with a random character inserted"""
        for url in s:
            pos = random.randint(0, len(url))
            random_character = chr(random.randrange(32, 127))
            url = url[:pos] + random_character + url[pos:]
        return s

    def _replace_random_character(self, s):
        """Returns s with a random character replaced"""
        if s == None:
            return None
        for url in s:
            pos = random.randint(0, len(url) - 1)
            random_character = chr(random.randrange(32, 127))
            url = url[:pos] + random_character + url[pos + 1 :]
        return s