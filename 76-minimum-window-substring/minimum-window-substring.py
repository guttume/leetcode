class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ns = len(s)
        nt = len(t)
        if ns < nt:
            return ""
        
        tCount = {}
        sCount = {}

        for i in range(nt):
            tCount[t[i]] = 1 + tCount.get(t[i], 0)
            sCount[s[i]] = 1 + sCount.get(s[i], 0)
            
        def checkInclusion():
            for key, value in tCount.items():
                if key not in sCount or sCount[key] < value:
                    return False

            return True

        ans = ""
        min_length = float("inf")
        l, r = 0, nt
        
        while r <= ns:
            if checkInclusion():
                current_length = r - l
                if current_length < min_length:
                    min_length = current_length
                    ans = s[l:r]
                
                l_key = s[l]    
                sCount[l_key] -= 1
                if sCount[l_key] == 0:
                    del(sCount[l_key])
                l += 1
            else:
                if r < ns:
                    r_key = s[r]
                    sCount[r_key] = 1 + sCount.get(r_key, 0)
                r += 1
                        
                    
        return ans




