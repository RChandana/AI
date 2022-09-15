# Implement Breadth First Search 
import collections
def breadth_first_search(graph, root) : 
    visited, queue = set(), collections.deque([root])
    visited.add(root)

    while queue : 
        vertex = queue.popleft()
        print(str(vertex) + " ", end = "")

        for neighbour in graph[vertex] :
            if neighbour not in visited : 
                visited.add(neighbour)
                queue.append(neighbour)

if __name__ == '__main__' : 
    graph = {0 : [1, 2], 1 : [3], 2 : [4], 3 : [1, 2], 4 : [2, 3]}
    print("The Breadth First Search is : ")
    breadth_first_search(graph, 0) 
