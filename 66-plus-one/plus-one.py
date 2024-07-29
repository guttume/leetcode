class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry, digit = divmod(digits[-1] + 1, 10)
        ans = [digit]

        for i in range(len(digits) - 2, -1, -1):
            carry, digit = divmod(digits[i] + carry, 10)            
            ans = [digit] + ans

        if carry > 0:
            ans =  [carry] + ans

        return ans