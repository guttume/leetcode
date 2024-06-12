class Solution:
    def climbStairs(self, n: int) -> int:
        if n  == 1:
            return 1

        if n == 2:
            return 2

        prev = 2
        prevPrev = 1

        for i in range(3, n + 1):
            current = prev + prevPrev
            prevPrev = prev
            prev = current

        return prev