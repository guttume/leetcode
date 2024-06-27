class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[] for i in range(numRows)]
        ans[0].append(1)

        for i in range(1, numRows):
            for j in range(i+1):
                top_first = j - 1
                top_second = j
                first = 0
                second = 0
                if top_first >= 0:
                    first = ans[i - 1][top_first]

                if top_second < i:
                    second = ans[i-1][top_second]

                ans[i].append(first + second)

        return ans