
class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []
        self.n = 0
        self.median = 0

    def addNum(self, num: int) -> None:
        
        self.n += 1
       
        if num <= self.median:
            heapq.heappush(self.left, -num) # max heap
            
            even = self.n%2 == 0
            len_diff = len(self.left) - len(self.right)
            
            # rebalance
            if (even and len_diff >= 1) or (not even and len_diff >= 2):
                n = -heapq.heappop(self.left)  
                heapq.heappush(self.right, n) # min heap

        else:
            heapq.heappush(self.right, num) # min heap
            
            even = self.n%2 == 0
            len_diff = len(self.right) - len(self.left)
            
            # rebalance
            if (even and len_diff >= 1) or (not even and len_diff >= 2):
                n = heapq.heappop(self.right)  
                heapq.heappush(self.left, -n) # max heap
            
        if len(self.left) > len(self.right):
            self.median = -self.left[0]
        elif len(self.left) < len(self.right):
            self.median = self.right[0]
        else:
            self.median = 0.5*(-self.left[0] + self.right[0])
            
        #print(self.left, self.right)
            
            
    def findMedian(self) -> float:
        return self.median


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()