class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        i = 0
        ans = 0

        for j, ch in enumerate(s):
            if ch in last_seen and last_seen[ch] >= i:
                i = last_seen[ch] + 1

            last_seen[ch] = j

            ans = max(ans, j - i + 1)

        return ans