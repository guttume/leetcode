class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)

        fractions = []

        for i in range(n):
            for j in range(i+1, n):
                heappush(fractions, (arr[i]/arr[j], [arr[i],arr[j]]))

        for i in range(k):
            ans = heappop(fractions)

        return ans[1]

        

        