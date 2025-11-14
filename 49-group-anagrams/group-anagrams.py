class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        tracker = defaultdict(list)

        for word in strs:
            key = tuple(sorted(word))
            tracker[key].append(word)

        ans = []

        for values in tracker.values():
            ans.append(values)

        return ans