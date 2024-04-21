class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def isPermutation(s, t):
            if len(s) != len(t):
                return False

            return sorted(s) == sorted(t)
        
        for i in range(len(s2) - len(s1) + 1):
            if isPermutation(s1, s2[i:i+len(s1)]):
                return True

        return False



