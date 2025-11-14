class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        seen = set()

        i = 0
        j = 0

        while j < len(s):
            if s[j] in seen:
                ans = max(ans, j - i)
                while s[i] != s[j]:
                    seen.remove(s[i])
                    i += 1
                seen.remove(s[i])
                i += 1

            seen.add(s[j])
            j += 1

        return max(ans, j - i)