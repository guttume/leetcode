class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        tracker = [0] * 26

        for letter in s:
            tracker[ord(letter)-ord('a')] += 1

        for letter in t:
            tracker[ord(letter)-ord('a')] -= 1

        for letter in tracker:
            if letter != 0:
                return False

        return True