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
