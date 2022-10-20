# This code uses Travelling Salesman Problem to solve the Hill Climbing Algorithm

import random
def random_Solution(travelling_salesman_problem):
    cities = list(range(len(travelling_salesman_problem)))
    solution = []

    for i in range(len(travelling_salesman_problem)):
        random_City = cities[random.randint(0, len(cities) - 1)]
        solution.append(random_City)
        cities.remove(random_City)

    return solution
