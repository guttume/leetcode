class Solution:
    def getLucky(self, s: str, k: int) -> int:
        ints = ""

        for c in s:
            ints += str(ord(c) - ord('a') + 1)

        ints = int(ints)

        
        while k > 0:
            ans = 0
            while ints > 0:
                ints, rem = divmod(ints, 10)
                ans += rem
            k -= 1
            ints = ans

        return ints

        
