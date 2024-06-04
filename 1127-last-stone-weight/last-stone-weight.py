class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        inverted_stones = [-1 * stone for stone in stones]
        heapq.heapify(inverted_stones)
        while len(inverted_stones) > 1:
            y = heapq.heappop(inverted_stones) * -1
            x = heapq.heappop(inverted_stones) * -1
            a = y - x
            heapq.heappush(inverted_stones, a * -1)

        return inverted_stones[0] * -1
