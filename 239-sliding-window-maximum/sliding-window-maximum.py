class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        r = 0
        
        q = deque()
        ans = []
        
        while r < len(nums):
            while len(q) > 0 and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            if r - l + 1 == k:
                ans.append(nums[q[0]])
                if q[0] == l:
                    q.popleft()
                l += 1
            r += 1
                
        return ans