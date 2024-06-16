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
                
            value = nums[i]
            nextNext = i - 2
            nextn = i - 1
            take = value + helper(nextNext, j)
            skip = helper(nextn, j)

            memo[(i, j)] = max(take, skip)
            return memo[(i, j)]

        return max(helper(n-2, 0), helper(n-1, 1))