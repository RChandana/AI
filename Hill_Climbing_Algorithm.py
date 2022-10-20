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

def route_Length(travelling_salesman_problem, solution):
    route_Length = 0
    for i in range(len(solution)):
        route_Length += travelling_salesman_problem[solution[i - 1]][solution[i]]
    return route_Length

def get_Neighbours(solution):
    neighbours = []
    for i in range(len(solution)):
        for j in range(i + 1, len(solution)):
            neighbour = solution.copy()
            neighbour[i] = solution[j]
            neighbour[j] = solution[i]
            neighbours.append(neighbour)
    return neighbours
