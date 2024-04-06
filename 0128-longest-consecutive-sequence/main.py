from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s: set = set(nums)

        most = 0
        for num in nums:
            if num - 1 not in s:
                next = num + 1
                current_max = 1

                while next in s:
                    current_max+=1
                    next+=1

                most = max(current_max, most)

        return most