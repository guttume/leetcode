class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        scounter, tcounter = 0, 0
        ans = 0

        while scounter < len(s) and tcounter < len(t):
            if s[scounter] == t[tcounter]:
                tcounter += 1
            scounter += 1

        if tcounter < len(t):
            for i in range(tcounter, len(t)):
                ans += 1

        return ans
            