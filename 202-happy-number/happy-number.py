class Solution:
    def isHappy(self, n: int) -> bool:

        def sum_of_digit(n):
            sumd = 0

            while n > 0:
                sumd += (n % 10) ** 2
                n = n // 10

            return sumd

        slow, fast = n, sum_of_digit(n)

        while slow != fast:
            fast = sum_of_digit(fast)
            fast = sum_of_digit(fast)
            slow = sum_of_digit(slow)

        return True if fast == 1 else False
        