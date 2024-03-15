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
            self._replace_body_content,
            self._replace_random_character
        ]
        mutator = np.random.choice(possible_mutations)

        return mutator(x)

    def _delete_random_character(self, s):
        """Returns s with a random character deleted"""
        for html in s:
            if len(html) > 5:
                pos = random.randint(0, len(html) - 1)
                html = html[:pos] + html[pos + 1 :]
        return s

    def _replace_random_character(self, s):
        """Returns s with a random character replaced"""
        for html in s:
            pos = random.randint(0, len(html) - 1)
            random_character = chr(random.randrange(32, 127))
            html = html[:pos] + random_character + html[pos + 1 :]
        return s

    def _replace_body_content(self, s):
        """Replaces content within the <body> tag with a random string"""
        for html in s:
            start = html.find("<body>") + len("<body>")
            end = html.find("</body>")
            if start != -1 and end != -1:
                html = html[:start] + self._generate_random_html_content() + html[end:]
        return s

    def _generate_random_html_content(self):
        """Generates random HTML content"""
        # You can customize this method based on your requirements
        return "<p>" + "".join(random.choices("abcdefghijklmnopqrstuvwxyz", k=10)) + "</p>"