class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        def helper(nums):
            m = len(nums)

            if m == 1:
                return nums[0]

            dp = [0] * 2

            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])

            for i in range(2, m):
                temp = max(nums[i] + dp[0], dp[1])
                dp[0] = dp[1]
                dp[1] = temp

            return dp[1]

        return max(helper(nums[:-1]), helper(nums[1:]))