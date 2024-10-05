class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        c = 0
        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = -1
                c += 1
        
        i, j = 0, len(nums) - 1
        while i < j:
            if nums[j] == -1:
                j -= 1
            elif nums[i] == -1:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            else:
                i += 1
        
        return len(nums) - c
        

        