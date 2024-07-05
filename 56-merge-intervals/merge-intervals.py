class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []

        intervals.sort()
        newInterval = intervals[0]

        for i in range(1, len(intervals)):
            current = intervals[i]

            if current[0] > newInterval[1]:
                ans.append(newInterval)
                newInterval = current
            elif current[1] < newInterval[0]:
                ans.append(current)
            else:
                newInterval = [min(newInterval[0], current[0]), max(newInterval[1], current[1])]

        ans.append(newInterval)

        return ans
