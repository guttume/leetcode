class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort()

        ans = 0

        for i in range(k):
            l = happiness.pop()
            l = max(l-i, 0)
            ans += l

        return ans