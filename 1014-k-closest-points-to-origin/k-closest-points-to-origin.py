class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        x2 = 0
        y2 = 0
        ans = []

        for point in points:
            x1 = point[0]
            y1 = point[1]
            distance = math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))
            heapq.heappush(heap, (distance, point))

        while k > 0:
            distance, point = heapq.heappop(heap)
            ans.append(point)
            k -= 1

        return ans