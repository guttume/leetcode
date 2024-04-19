class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n < 2:
            return n
        left, right = 0, 1
        window = set(s[left])
        max_length = 0

        current_length = 1
        while right < len(s):
            if s[right] in window:
                window.remove(s[left])
                left += 1
                current_length -= 1
            else:
                window.add(s[right])
                right += 1
                current_length += 1
                max_length = max(max_length, current_length)

        return max(max_length, current_length)