from numpy import ndarray
from poly_sbst.generators.abstract_generator import AbstractGenerator
from poly_sbst.common.abstract_grammar import AbstractGrammar
import numpy as np
import random

class HTMLTestSuiteGenerator(AbstractGenerator):
    """
    A class that generates test suites using a HTML grammar generator.

    Attributes:
        _name (str): The name of the generator.
        max_length (int): The maximum length of the test suite.
        min_length (int): The minimum length of the test suite.
    """

    def __init__(self) -> None:
        super().__init__()
        self._name = "HTMLTestSuiteGenerator"
        self.max_length = 10
        self.min_length = 2

    @property
    def name(self) -> int:
        return self._name

    def generate_random_html(self) -> str:
        """
        Generate a random HTML test suite.

        Returns:
            str: The HTML generated test suite.
        """
        html = "<html>\n"
        html += self._generate_random_element()
        html += "</html>"
        return html

    def _generate_random_element(self):
        tags = ["<div>", "<p>", "<span>", "<header>", "<footer>", "<section>", "<article>", "<aside>", "<nav>", "<ul>", "<ol>", "<li>", "<h1>", "<h2>", "<h3>", "<h4>", "<h5>", "<h6>", "<a>"]
        tag = random.choice(tags)
        content = self._generate_random_content()
        return f"{tag}{content}</{tag[1:]}>\n"

    def _generate_random_content(self):
        contents = ["Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
                    "Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
                    "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
                    "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.",
                    "Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."]
        content = ""
        content += random.choice(contents)
        return content

    def generate_random_test(self) -> str:
        """
        Generate a random test suite.

        Returns:
            str: The HTML generated test suite.
        """
        html_grammar = {
            "<start>": ["<html>"],
            "<html>": ["<head>", "<body>"],
            "<head>": ["<title>", "<meta>", "<script>"],
            "<title>": ["<title_tag>"],
            "<title_tag>": ["Welcome", "About Us", "Contact Us", "Home"],
            "<meta>": ["<meta_tag>"],
            "<meta_tag>": ['<meta charset="UTF-8">', '<meta name="description" content="Description">', '<meta name="keywords" content="keyword1, keyword2, keyword3">'],
            "<script>": ['<script src="script.js"></script>'],
            "<body>": ["<header>", "<main>", "<footer>"],
            "<header>": ["<h1>", "<h2>"],
            "<h1>": ["Welcome", "About Us", "Contact Us"],
            "<h2>": ["Our Services", "Our Team", "Testimonials"],
            "<main>": ["<p>", "<img>", "<div>"],
            "<p>": ["<p_content>"],
            "<p_content>": ["Lorem ipsum dolor sit amet, consectetur adipiscing elit.", "Nulla facilisi. Vestibulum in fermentum justo."],
            "<img>": ['<img src="image.jpg" alt="Image">'],
            "<div>": ["<div_content>"],
            "<div_content>": ["<p><img>", "<h2><p>", "<p><h3>"],
            "<footer>": ["<p>"],
        }

        n = random.randint(self.min_length, self.max_length)
        test_suite = []
        for i in range(n):
            test_suite.append(self.generate_random_html())

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