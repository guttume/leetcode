class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        inverted_nums = [-num for num in nums]
        heapq.heapify(inverted_nums)
        while k > 1:
            heapq.heappop(inverted_nums)
            k -= 1
        
        return -heapq.heappop(inverted_nums)