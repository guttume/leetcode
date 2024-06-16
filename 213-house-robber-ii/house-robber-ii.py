class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(nums):
            if len(nums) == 0:
                return 0

            if len(nums) == 1:
                return nums[0]

            rob1 = nums[0]
            rob2 = max(nums[0], nums[1])

            for i in range(2, len(nums)):
                curr = max(rob2, nums[i] + rob1)
                rob1 = rob2
                rob2 = curr

            return max(rob1, rob2)
        
        n = len(nums)

        if n == 0:
            return 0

        if n == 1:
            return nums[0]

        take = nums[0] + helper(nums[2:-1])
        notake = 0 + helper(nums[1:])

        return max(take, notake)