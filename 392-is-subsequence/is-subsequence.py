class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0: return True
        if len(t) == 0: return False
        j = 0
        for c in s:
            found = False
            while j < len(t):
                current = t[j]
                j += 1
                if c == current:
                    found = True
                    break

        return found