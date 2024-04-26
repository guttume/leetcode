class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Counter = [0] * 26
        s2Counter = [0] * 26

        left, right = 0, len(s1) - 1
        
        for i in range(len(s1)):
            s1Counter[ord(s1[i]) - ord('a')] += 1
            s2Counter[ord(s2[i]) - ord('a')] += 1

        while right < len(s2):
            matches = 0
            for i in range(0, 26):
                if s1Counter[i] == s2Counter[i]:
                    matches += 1
            if matches == 26:
                return True
            
            if right == len(s2) -1:
                break
            
            s2Counter[ord(s2[left]) - ord('a')] -= 1
            left += 1
            right += 1
            s2Counter[ord(s2[right]) - ord('a')] += 1
            
        return False

        




