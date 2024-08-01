class Solution:
    def isHappy(self, n: int) -> bool:

        def sum_of_digit(n):
            sumd = 0

            while n > 0:
                sumd += (n % 10) ** 2
                n = n // 10

            return sumd

        sums = set()

        s = sum_of_digit(n)
        while s != 1:
            if s in sums:
                return False

            sums.add(s)
            s = sum_of_digit(s)

        return True
        