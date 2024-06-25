class Solution:
    def numDecodings(self, s: str) -> int:

        cache = {len(s): 1}

        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                cache[i] = 0
            else:
                cache[i] = cache[i + 1]

            if i + 1 < len(s) and (s[i] == "1" or (s[i] == "2" and s[i + 1] in "0123456")):
                cache[i] += cache[i + 2]

        return cache[0]

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