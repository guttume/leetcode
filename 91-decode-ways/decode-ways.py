class Solution:
    def numDecodings(self, s: str) -> int:
        cache = {len(s): 1}
        def dfs(i):
            if i in cache:
                return cache[i]

            if s[i] == "0":
                return 0

            takeOne = dfs(i+1)
            takeTwo = 0
            if i + 1 < len(s) and (s[i] == "1" or (s[i] == "2" and s[i + 1] in "0123456")):
                takeTwo = dfs(i+2)

            cache[i] = takeOne + takeTwo
            
            return cache[i]

        return dfs(0)