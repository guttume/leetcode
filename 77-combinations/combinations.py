class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        ans = []

        def backtrack(i, current):
            if i > n:
                return

            if len(current) == k:
                ans.append(current.copy())
                return

            for j in range(i + 1, n + 1):
                current.append(j)
                backtrack(j, current)
                current.pop()

        for i in range(1, n + 1):
            backtrack(i, [i])

        return ans