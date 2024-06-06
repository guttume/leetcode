class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        ans = []

        for x, y in points:
            distance = (x ** 2) + (y ** 2)
            heapq.heappush(heap, (distance, [x, y]))

        while k > 0:
            _, point = heapq.heappop(heap)
            ans.append(point)
            k -= 1

        return ans