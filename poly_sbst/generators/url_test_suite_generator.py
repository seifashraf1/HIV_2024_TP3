from numpy import ndarray
from poly_sbst.generators.abstract_generator import AbstractGenerator
from poly_sbst.common.abstract_grammar import AbstractGrammar
import numpy as np
import random

class UrlTestSuiteGenerator(AbstractGenerator):
    """
    A class that generates test suites using a url grammar generator.

    Attributes:
        _name (str): The name of the generator.
        max_length (int): The maximum length of the test suite.
        min_length (int): The minimum length of the test suite.
    """

    def __init__(self) -> None:
        super().__init__()
        self._name = "UrlTestSuiteGenerator"
        self.max_length = 5000
        self.min_length = 2

    @property
    def name(self) -> int:
        return self._name

    def generate_random_test(self) -> str:
        """
        Generate a random test suite.

        Returns:
            str: The Url generated test suite.
        """
        url_parse_grammar = {
            "<start>": ["<url>"],
            "<url>": ["<scheme>://<netloc>/<path>?<query>"],
            "<scheme>": ["http", "https", "ftp"],
            "<netloc>": ["<hostname>:<port>"],
            "<hostname>": ["www.<string>.<tld>"],
            "<string>": ["<char><string>", "<char>"],
            "<tld>": ["com", "org", "net", "edu", "gov"],
            "<port>": ["80", "443", "8080"],
            "<digit>": ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
            "<path>": ["/<segment>"],
            "<segment>": ["<identifier>", "<identifier>/<segment>"],
            "<identifier>": ["<char>", "<char><identifier>"],
            "<string>": ["<char><string>", "<char>"],
            "<char>": ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "-", "_", ".", "!", "~", "*", "'", "(", ")"],
            "<query>": ["<param>=<value>&<query>", "<param>=<value>"],
            "<param>": ["key1", "key2"],
            "<value>": ["value1", "value2"],
            "<fragment>": ["section1", "section2"]
        }

        url_grammar = AbstractGrammar(url_parse_grammar)

        n = random.randint(self.min_length, self.max_length)
        test_suite = []
        for i in range(n):
            test_suite.append(url_grammar.generate_input())

        return np.array(test_suite)

    def cmp_func(self, x: np.ndarray, y: np.ndarray) -> float:
        """
        Compare two test cases and return a similarity score.

        Args:
            x (np.ndarray): The first test case.
            y (np.ndarray): The second test case.

        Returns:
            float: The similarity score between the two test cases.
        """
        return 0.0