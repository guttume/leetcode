class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        leftSum = [0] * n
        rightSum = [0] * n
        ans = [0] * n

        runningTotal = 0
        for i in range(1, n):
            leftSum[i] = runningTotal + nums[i - 1]
            runningTotal = leftSum[i]

        runningTotal = 0
        for i in range(n - 2, -1, -1):
            rightSum[i] = runningTotal + nums[i + 1]
            runningTotal = rightSum[i]

        for i in range(n):
            ans[i] = abs(leftSum[i] - rightSum[i])

        return ans