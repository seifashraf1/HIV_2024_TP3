

from datetime import datetime
from poly_sbst.common.random_seed import get_random_seed
from poly_sbst.common.abstract_executor import AbstractExecutor
from poly_sbst.problems.random_problem import RandomProblem
from poly_sbst.generators.random_generator import RandomGenerator
from pymoo.algorithms.soo.nonconvex.ga import GA
from pymoo.algorithms.soo.nonconvex.random_search import RandomSearch
from poly_sbst.sampling.abstract_sampling import AbstractSampling
from poly_sbst.mutation.random_mutation import RandomMutation
from poly_sbst.crossover.random_crossover import OnePointCrossover
from poly_sbst.problems.test_suite_problem import TestSuiteProblem
from poly_sbst.generators.test_suite_generator import TestSuiteGenerator
from poly_sbst.mutation.test_suite_mutation import TestSuiteMutation
from pymoo.optimize import minimize
from urllib.parse import urlparse
from html.parser import HTMLParser

def optimize(runs=1):

    now = datetime.now()
    dt_string = now.strftime("%d-%m-%Y")

    for run in range(runs):

        seed = get_random_seed()
        pop_size = 10
        num_gen = 5

        generator = TestSuiteGenerator() #RandomGenerator() #

        executor = AbstractExecutor(HTMLParser().feed) #HTMLParser().feed #cgi_decode
        problem = TestSuiteProblem(executor) #RandomProblem(executor=executor) #
        
        method = GA(pop_size=pop_size,
                n_offsprings=int(pop_size/2),
                sampling=AbstractSampling(generator),#FloatRandomSampling(),
                mutation=TestSuiteMutation(generator=generator),#,#, (prob=0.4, eta=3.0, vtype=float) #(prob=0.4, eta=3.0, vtype=float),RandomMutation(mut_rate=0.4)
                crossover=OnePointCrossover(cross_rate=0.9),#OnePointCrossover(cross_rate=0.9),
                eliminate_duplicates=False
                )
        
        res = minimize(problem,
                method,
                termination=('n_gen', num_gen),#BeamNGTermination(),#
                seed=seed,
                verbose=True,
                eliminate_duplicates=False,
                save_history=True
                )
        
        print("Best solution found: %s" % res.X)
        print("Function value: %s" % res.F)
        print("Execution data:", res.problem.execution_data)
        #log.info(f"Executor data {executor.test_dict}")


if __name__ == "__main__":
    optimize()
        