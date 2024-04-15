class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def time_to_eat(k):
            tt = 0
            for p in piles:
                tt += (p - 1) // k + 1
                
            return tt

        left, right = 1, max(piles)
        ans = right
        while left <= right:
            mid = (left + right) // 2

            tt = time_to_eat(mid)
            
            if tt <= h:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return ans



