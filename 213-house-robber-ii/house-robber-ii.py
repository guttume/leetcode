class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        memo = {}

        def helper(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            if i < j:
                return 0

            if i == j:
                return nums[i]
            
            memo[(i, j)] = max(nums[i] + helper(i - 2, j), helper(i - 1, j))
            return memo[(i, j)]

        return max(helper(n-2, 0), helper(n-1, 1))