from queue import PriorityQueue
from re import T
nodes = 14
graph = [[] for i in range(nodes)]

def best_first_search(actual_Src, target, n) : 
    visited = [False] * n
    priority_queue = PriorityQueue()
    priority_queue.put((0, actual_Src))
    visited[actual_Src] = True

    while priority_queue.empty() == False : 
        a = priority_queue.get()[1]
        print(a, end = " ")
        if a == target : 
            break
        for v, c in graph[a] : 
            if visited[v] == False : 
                visited[v] = True
                priority_queue.put((c, v))
    print()

def add_edge(x, y, cost) :
    graph[x].append((y, cost))      
    graph[y].append((x, cost))       
