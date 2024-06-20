class Solution:
    def clearDigits(self, s: str) -> str:
        ans = ""
        count = 0
        
        for i in range(len(s) - 1, -1, -1):
            if s[i] >= '0' and s[i] <= '9':
                count += 1
            elif count == 0:
                ans = s[i] + ans
            else:
                count -= 1

        return ans