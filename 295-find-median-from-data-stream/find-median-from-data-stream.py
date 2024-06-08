class MedianFinder:

    def __init__(self):
        self.maxHeap = []
        self.minHeap = []

    def addNum(self, num: int) -> None:
        if self.minHeap and num > self.minHeap[0]:
            heapq.heappush(self.minHeap, num)
        else:
            heapq.heappush(self.maxHeap, num * -1)

        if len(self.maxHeap) - len(self.minHeap) > 1:
            val = heapq.heappop(self.maxHeap) * -1
            heapq.heappush(self.minHeap, val)
        elif len(self.minHeap) - len(self.maxHeap) > 1:
            val = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, val * -1)

    def findMedian(self) -> float:
        if len(self.maxHeap) > len(self.minHeap):
            return self.maxHeap[0] * -1
        
        if len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]

        return ((self.maxHeap[0] * -1) + self.minHeap[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()