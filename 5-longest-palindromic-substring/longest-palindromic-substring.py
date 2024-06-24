class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        longest = s[0]

        for i in range(len(s)):
            l= r = i
            current = ""
            while l >= 0 and r < len(s) and s[l] == s[r]:
                current = s[l] + current
                if l != r:
                    current += s[r]
                l -= 1
                r += 1

            if len(longest) < len(current):
                longest = current

            current = ""
            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                current = s[l] + current
                current += s[r]
                l -= 1
                r += 1

            if len(longest) < len(current):
                longest = current


        return longest