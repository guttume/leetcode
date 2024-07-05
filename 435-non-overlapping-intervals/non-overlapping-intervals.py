class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])

        ans = 0
        currentI = intervals[0]

        for i in range(1, len(intervals)):
            nextI = intervals[i]

            if nextI[0] < currentI[1]:
                ans += 1
                if currentI[1] > nextI[1]:
                    currentI = nextI

            else:
                currentI = nextI

        return ans
                    

