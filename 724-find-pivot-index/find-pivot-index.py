class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0] * n
        suffix = [0] * n

        sum = 0
        for i in range(1, n):
            prefix[i] = nums[i - 1] + sum
            sum = prefix[i]

        sum = 0
        for i in range(n - 2, -1 , -1):
            suffix[i] = nums[i + 1] + sum
            sum = suffix[i]
            
        for i in range(n):
            if prefix[i] == suffix[i]:
                return i
        
        return -1