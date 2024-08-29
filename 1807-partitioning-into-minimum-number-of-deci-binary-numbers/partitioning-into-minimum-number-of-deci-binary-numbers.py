class Solution:
    def minPartitions(self, n: str) -> int:
        max_i = int(n[0])

        for i in n:
            max_i = max(max_i, int(i))

        return max_i