class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = collections.Counter(s)

        ans = 0
        take = True
        for i in count.values():
            if i % 2 == 0:
                ans += i
            else:
                ans += (i - 1)
                if take:
                    ans += 1
                    take = False

        return ans
                    
        
        return ans