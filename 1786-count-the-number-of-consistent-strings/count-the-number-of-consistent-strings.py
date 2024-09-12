class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)

        count = 0
        for w in words:
            consistent = True
            for c in w:
                if c not in allowed:
                    consistent = False

            if consistent:
                count += 1

        return count 