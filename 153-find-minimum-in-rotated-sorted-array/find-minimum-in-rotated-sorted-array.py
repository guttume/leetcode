class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        elif n == 2:
            return nums[0] if nums[0] < nums[1] else nums[1]

        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                return nums[i + 1]

        return nums[0]