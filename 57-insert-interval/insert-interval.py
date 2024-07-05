class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []

        for i in range(len(intervals)):
            interval = intervals[i]
            if interval[0] > newInterval[1]:
                ans.append(newInterval)
                return ans + intervals[i:]

            if interval[1] < newInterval[0]:
                ans.append(interval)
            else:
                newInterval = [min(interval[0], newInterval[0]), max(interval[1], newInterval[1])]

        ans.append(newInterval)

        return ans

            