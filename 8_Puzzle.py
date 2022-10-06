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
