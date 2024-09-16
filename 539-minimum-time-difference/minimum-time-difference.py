class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        # Convert timePoints to minutes since midnight
        minutes = []
        for time in timePoints:
            dt = datetime.datetime.strptime(time, "%H:%M")
            minutes_since_midnight = dt.hour * 60 + dt.minute
            minutes.append(minutes_since_midnight)
        
        # Sort the list of minutes
        minutes.sort()
        
        # Find the minimum difference
        min_diff = float('inf')
        for i in range(len(minutes)):
            next_time = (i + 1) % len(minutes)  # Circular difference
            diff = (minutes[next_time] - minutes[i]) % (24 * 60)
            min_diff = min(min_diff, diff)
        
        return min_diff
