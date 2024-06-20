class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        
        w = 0
        c = 0

        for i in range(1, len(skills)):
            if c == k:
                return w

            if skills[w] > skills[i]:
                c += 1
            else:
                w = i
                c = 1

        return w
