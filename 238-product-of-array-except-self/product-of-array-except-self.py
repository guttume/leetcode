class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        
        prefix = [nums[0]] * len(nums)
        for i in range(1, len(nums)):
            prefix[i] = nums[i] * prefix[i-1]
            
        suffix = [nums[-1]] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = nums[i] * suffix[i + 1]
            
        ans[0] = suffix[1]
        ans[-1] = prefix[-2]
        
        for i in range(1, len(nums)-1):
            ans[i] = prefix[i - 1] * suffix[i + 1]
            
        return ans