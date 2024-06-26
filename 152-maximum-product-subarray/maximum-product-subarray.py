class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prefix = 1
        suffix = 1
        maxi = float("-inf")
        n = len(nums)

        for i in range(n):
            prefix = prefix * nums[i]
            suffix = suffix * nums [n - i - 1]
            maxi = max(maxi, prefix, suffix)

            if nums[i] == 0:
                prefix = 1

            if nums[n - i - 1] == 0:
                suffix = 1

        return maxi

            