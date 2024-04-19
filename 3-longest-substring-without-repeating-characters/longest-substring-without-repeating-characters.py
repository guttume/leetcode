class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        window = set()
        max_length = 0

        while right < len(s):
            if s[right] not in window:
                window.add(s[right])
                right += 1
                max_length = max(max_length, len(window))
            else:
                window.remove(s[left])
                left += 1

        return max_length