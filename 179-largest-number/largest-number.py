class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        s_nums = [str(num) for num in nums]

        s_nums.sort(key=lambda a: a * 10, reverse=True)

        if s_nums[0] == "0":
            return "0"

        return "".join(s_nums)

