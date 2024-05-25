class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        stack = [(0, [], 0)]  # Initialize stack with (start_index, current_combination, total_sum)

        while stack:
            start, cur, total = stack.pop()
            
            if total == target:
                ans.append(cur[:])  # Append a copy of the current combination to the answer
                continue
                
            if total > target or start >= len(candidates):
                continue

            # Iterate through candidates starting from 'start' index to explore all combinations
            for i in range(start, len(candidates)):
                # Include the current candidate
                cur.append(candidates[i])
                stack.append((i, cur[:], total + candidates[i]))
                # Backtrack by removing the last candidate
                cur.pop()

        return ans
