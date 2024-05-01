class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        keeper = collections.deque()
        ans = []

        l, r = 0, 0

        while r < len(nums):
            while len(keeper) > 0 and nums[keeper[-1]] < nums[r]:
                keeper.pop()

            keeper.append(r)

            r += 1
            cw = r - l + 1
            if cw > k:
                l += 1
                ans.append(nums[keeper[0]]) 
                if len(keeper) > 0 and keeper[0] == l - 1:
                    keeper.popleft()

        return ans