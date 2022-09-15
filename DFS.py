# Implement Depth First Search
def dfs(graph, start, visited = None):
    if visited is None:
        visited = set()
    visited.add(start)

    print(start)

    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited


graph = {'0' : set(['1', '2', '3']),
         '1' : set(['0', '3', '4', '5']),
         '2' : set(['0']),
         '3' : set(['1']),
         '4' : set(['2', '3', '4']),
         '5' : set(['3', '4', '5'])}

dfs(graph, '0')
