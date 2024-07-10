class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
            
        step_needed = 1
        for i in range(len(nums) - 2, 0, -1):
            current = nums[i]

            if current >= step_needed:
                step_needed = 1
            else:
                step_needed += 1

        return nums[0] >= step_needed

            