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
add_edge(0, 1, 4)
add_edge(0, 2, 8)
add_edge(0, 4, 5)
add_edge(1, 3, 9)
add_edge(1, 5, 6)
add_edge(2, 8, 12)
add_edge(2, 7, 14)
add_edge(4, 6, 7)
add_edge(6, 9, 5)
add_edge(6, 10, 8)
add_edge(9, 11, 1)
add_edge(9, 12, 10)
add_edge(9, 13, 2)

start_node = 0
goal_node = 13

best_first_search(start_node, goal_node, nodes)
print("\nThe initial node is : " , start_node )
print("\nThe goal node is : " , goal_node)
print("\nHence this algorithm is Best First Algorithm!!")
