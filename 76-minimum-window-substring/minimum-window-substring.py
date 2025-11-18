class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def is_t_in_s(s_counter, t_counter):
            for k, v in t_counter.items():
                if s_counter.get(k, 0) < v:
                    return False
                    
            return True

        if not s or not t:
            return ""
            
        l, r = 0, 0
        
        ans = ""
        min_count = float("inf")
        
        t_count = Counter(t)
        s_count = {}
        
        while r < len(s):
            s_count[s[r]] = 1 + s_count.get(s[r], 0)
            
            while is_t_in_s(s_count, t_count):
                if min_count > r - l + 1:
                    min_count = r - l + 1
                    ans = s[l:r+1]
                    
                s_count[s[l]] = s_count[s[l]] - 1
                if s_count[s[l]] == 0:
                    del(s_count[s[l]])
                l += 1
                

            r += 1
                        
        return ans