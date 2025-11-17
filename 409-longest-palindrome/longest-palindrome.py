class Solution:
    def longestPalindrome(self, s: str) -> int:
        c = Counter(s)

        ans = 0
        odd_used = False

        for i in c.values():
            if i % 2 == 0:
                ans += i
            else:
                ans += i - 1
                odd_used = True

        return ans + (1 if odd_used else 0)