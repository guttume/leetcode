class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = 0
        temp  =x

        while temp > 0:
            temp, q = divmod(temp, 10)
            y = y * 10 + q

        return y == x