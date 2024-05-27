class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def dfs(choices, cur):
            if len(choices) == 0:
                ans.append(cur[:])
                return

            for i in range(len(choices)):
                cur.append(choices[i])
                dfs(choices[:i] + choices[i+1:], cur)
                cur.pop()

        dfs(nums, [])

        return ans