class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        current_sum = 0

        for n in nums:
            current_sum = max(current_sum, 0)
            current_sum += n
            max_sum = max(max_sum, current_sum)
        
        return max_sum