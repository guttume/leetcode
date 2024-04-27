class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ns = len(s)
        nt = len(t)
        if ns < nt:
            return ""
        
        tCount = collections.Counter(t)
        sCount = collections.Counter(s[:nt])
        matches = 0

        for key, value in tCount.items():
            if key in sCount:
                matches += min(sCount[key], value)

        ans = ""
        min_length = float("inf")
        l, r = 0, nt
        
        while r <= ns:
            if matches >= nt:
                current_length = r - l
                if current_length < min_length:
                    min_length = current_length
                    ans = s[l:r]
                
                l_key = s[l]    
                sCount[l_key] -= 1
                if l_key in tCount and tCount[l_key] > sCount[l_key]:
                    matches -= 1
                if sCount[l_key] == 0:
                    del(sCount[l_key])
                l += 1
            else:
                if r < ns:
                    r_key = s[r]
                    sCount[r_key] = 1 + sCount.get(r_key, 0)
                    if r_key in tCount and sCount[r_key] <= tCount[r_key]:
                        matches += 1
                r += 1
                        
                    
        return ans




