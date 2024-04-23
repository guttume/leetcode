class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""

        shortest_string = len(strs[0])

        for s in strs:
            shortest_string = min(shortest_string, len(s))

        for i in range(shortest_string):
            char = strs[0][i]
            found = True
            for j in range(1, len(strs)):
                if char != strs[j][i]:
                    found = False
            if found:
                ans += char
            else:
                break

        return ans
