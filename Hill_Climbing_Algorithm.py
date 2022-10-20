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
def get_Best_Neighbour(travelling_salesman_problem, neighbours):
    best_Route_Length = route_Length(travelling_salesman_problem, neighbours[0])
    best_Neighbour = neighbours[0]
    for neighbour in neighbours:
        current_Route_Length = route_Length(travelling_salesman_problem, neighbour)
        if current_Route_Length < best_Route_Length:
            best_Route_Length = current_Route_Length
            best_Neighbour = neighbour
    return best_Neighbour, best_Route_Length

def hill_Climbing(travelling_salesman_problem):
    current_Solution = random_Solution(travelling_salesman_problem)
    current_Route_Length = route_Length(travelling_salesman_problem, current_Solution)
    neighbours = get_Neighbours(current_Solution)
    best_Neighbour, best_Neighbour_Route_Length = get_Best_Neighbour(travelling_salesman_problem, neighbours)
