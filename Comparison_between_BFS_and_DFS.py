# This code is for comparing between BFS and DFS Search Algorithms

graph = {
    'A': ['C', 'B'],
    'B': ['F', "G"],
    'C': ['D', "E"],
    'D': [],
    'E': ['I', 'H'],
    "F": [],
    'G': [],
    "H": [],
    'I': ['J', 'K'],
    'J': [],
    'K': ['L', 'M'],
    'L': [],
    'M': []
}

def breadth_first_search(visit_complete, graph, current_node):
    visit_complete.append(current_node)
    queue = [current_node]

    while queue:
        s = queue.pop(0)
        print(s)

        for neighbour in graph[s]:
            if neighbour not in visit_complete:
                visit_complete.append(neighbour)
                queue.append(neighbour)


print("Breadth first search algorithm: ")
breadth_first_search([], graph, 'A')

visited = set()
