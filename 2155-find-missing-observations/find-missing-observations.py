class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        total_rolls = n + len(rolls)
        
        r_sum = mean * total_rolls - sum(rolls)
        
        ans = [1] * n
        a_sum = sum(ans)
        if a_sum == r_sum:
            return ans
        
        for i in range(len(ans)):
            for j in range(2, 7):
                ans[i] = j
                a_sum += 1
                if a_sum == r_sum:
                    return ans
        
        return []