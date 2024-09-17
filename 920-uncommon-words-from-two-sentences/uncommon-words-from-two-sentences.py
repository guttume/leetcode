class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s = s1 + " " + s2

        freq = {}

        s = s.split(" ")

        for w in s:
            freq[w] = 1 + freq.get(w, 0)

        ans = []

        for k, v in freq.items():
            if v == 1:
                ans.append(k)

        return ans