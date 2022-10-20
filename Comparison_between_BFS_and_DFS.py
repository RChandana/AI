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

def depth_first_search(visited, graph, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            depth_first_search(visited, graph, neighbour)


print("Depth first search algorithm: ")
depth_first_search(visited, graph, 'A')
