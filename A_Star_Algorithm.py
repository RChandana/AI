from collections import deque
class Graph:
    def __init__(self, map):
        self.map = map

    def get_neighbors(self, v):
        return self.map[v]

    def h(self, n):
        H = {
            'A': 11,
            'B': 6,
            'C': 5,
            'D': 7,
            'E': 3,
            'F': 6,
            'G': 5,
            'H': 3,
            'I': 1,
            'J': 0
        }
        return H[n]
