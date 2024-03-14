#this is a dummy test file to test different stuff

from pymoo.algorithms.soo.nonconvex.ga import GA
from pymoo.problems import get_problem
from pymoo.optimize import minimize
from pymoo.config import Config
Config.warnings['not_compiled'] = False

from poly_sbst.mutation.url_test_suite_mutation import UrlTestSuiteMutation
from poly_sbst.generators.url_test_suite_generator import UrlTestSuiteGenerator

t = UrlTestSuiteMutation(generator=UrlTestSuiteGenerator())

s = ['ftp://www.1B.com:443//Wj0?key1=value1&key2=value1',
 'https://www.NSC.edu:8080//Z/UqM?key2=value1&key2=value1',
 'ftp://www.)p.com:80//u/Y(s8?key1=value1&key2=value1&key2=value1',
 'http://www.l.edu:8080//)m?key2=value1&key2=value2',
 'http://www.L8.edu:443//T6e/Xan?key2=value2',
 'http://www.0r.edu:80//Z/-/*/-ZIB?key1=value2&key2=value1']

print(t._delete_random_character(s))
print(t._insert_random_character(s))
print(t._replace_random_character(s))