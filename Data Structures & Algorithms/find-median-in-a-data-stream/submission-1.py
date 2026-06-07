class MedianFinder:

    def __init__(self):
        self.maxheap = []
        self.minheap = []
        
    def addNum(self, num: int) -> None:
        heapq.heappush(self.minheap, -num)
        
        if self.minheap and self.maxheap and -self.minheap[0] > self.maxheap[0]:
            val = heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap, -val)
                
        if len(self.maxheap) > len(self.minheap) + 1:
            val = heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap, -val)

        if len(self.minheap) > len(self.maxheap) + 1:
            val = heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap, -val)

    def findMedian(self) -> float:
        if len(self.minheap) > len(self.maxheap):
            return -self.minheap[0]
        elif len(self.maxheap) > len(self.minheap):
            return self.maxheap[0]
        else:
            return (-self.minheap[0]+self.maxheap[0])/2
        
        