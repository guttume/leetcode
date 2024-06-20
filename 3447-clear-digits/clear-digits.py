class Solution:
    def clearDigits(self, s: str) -> str:

        helper = [1] * len(s)

        for i in range(len(s)):
            if s[i] >= '0' and s[i] <= '9':
                helper[i] = 0
                
                for j in range(i - 1, -1 , -1):
                    if s[j] >= 'a' and s[j] <= 'z' and helper[j] == 1:
                        helper[j] = 0
                        break
        
        ans = ""
        for i in range(len(s)):
            if helper[i] == 1:
                ans += s[i]

        return ans