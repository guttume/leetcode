class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def helper(i, nums, sets, curSet):
            if i >= len(nums):
                sets.append(curSet.copy())
                return

            curSet.append(nums[i])
            helper(i + 1, nums, sets, curSet)
            curSet.pop()
            helper(i + 1, nums, sets, curSet)

        sets = []
        curSet = []
        helper(0, nums, sets, curSet)
        return sets

        

        