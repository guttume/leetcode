class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        def helper(i, j, memo):
            if (i, j) in memo:
                return memo[(i, j)]

            if i < j:
                return 0

            if i == j:
                return nums[i]
                
            value = nums[i]
            nextNext = i - 2
            nextn = i - 1
            take = value + helper(nextNext, j, memo)
            skip = helper(nextn, j, memo)

            memo[(i, j)] = max(take, skip)
            return memo[(i, j)]

        memo = {}
        return max(helper(n-2, 0, memo), helper(n-1, 1, memo))