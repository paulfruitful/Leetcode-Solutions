import heapq

class SmallestInfiniteSet:
    def __init__(self):
        self.heap = []
        self.addSet=set()
        self.counter = 1
        
    def popSmallest(self):
        if self.heap:
            smallest=heapq.heappop(self.heap)
            self.addSet.remove(smallest)
            return smallest
        num=self.counter
        self.counter+=1
        return num
    
    def addBack(self, num):
        if num<self.counter and num not in self.addSet:
         heapq.heappush(self.heap, num)
         self.addSet.add(num)
