import copy   
from heapq import heappush, heappop  
n = 3  
rows = [ 1, 0, -1, 0 ]  
cols = [ 0, -1, 0, 1 ]  
class priorityQueue:  
    def __init__(self):  
        self.heap = []  
    def push(self, key):  
        heappush(self.heap, key)  
    def pop(self):  
        return heappop(self.heap)  
    def empty(self):  
        if not self.heap:  
            return True  
        else:  
            return False  
class nodes:  
    def __init__(self, parent, mats, empty_tile_posi, costs, levels):  
        self.parent = parent  
        self.mats = mats   
        self.empty_tile_posi = empty_tile_posi  
        self.costs = costs  
        self.levels = levels  
    def __lt__(self, nxt):  
        return self.costs < nxt.costs  
   
def calculateCosts(mats, final) -> int:  
      
    count = 0  
    for i in range(n):  
        for j in range(n):  
            if ((mats[i][j]) and  
                (mats[i][j] != final[i][j])):  
                count += 1  
                  
    return count  
def newNodes(mats, empty_tile_posi, new_empty_tile_posi, levels, parent, final) -> nodes:  
    new_mats = copy.deepcopy(mats)  
    x1 = empty_tile_posi[0]  
    y1 = empty_tile_posi[1]  
    x2 = new_empty_tile_posi[0]  
    y2 = new_empty_tile_posi[1]  
    new_mats[x1][y1], new_mats[x2][y2] = new_mats[x2][y2], new_mats[x1][y1]  
  
    costs = calculateCosts(new_mats, final)  
  
    new_nodes = nodes(parent, new_mats, new_empty_tile_posi, costs, levels)  
    return new_nodes  
def printMatsrix(mats):  
      
    for i in range(n):  
        for j in range(n):  
            print("%d " % (mats[i][j]), end = " ")
       
def isSafe(x, y):  
      
    return x >= 0 and x < n and y >= 0 and y < n  
   
def printPath(root):  
      
    if root == None:  
        return  
      
    printPath(root.parent)  
    printMatsrix(root.mats)  
    print()
