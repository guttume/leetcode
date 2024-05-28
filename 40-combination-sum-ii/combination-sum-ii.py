class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        stack = [(0, [], 0)]
        candidates.sort()

        while stack:
            start, cur, total = stack.pop()

            if total == target:
                ans.append(cur[:])
                continue

            if total > target or start >= len(candidates):
                continue

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                if total + candidates[i] > target:
                    break

                stack.append((i + 1, cur + [candidates[i]], total + candidates[i]))

        return ans
