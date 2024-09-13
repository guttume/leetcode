class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        ans = []

        prefix_xor = [0] * (len(arr)+1)
        for i in range(len(arr)):
            prefix_xor[i+1] = prefix_xor[i] ^ arr[i]

        for left, right in queries:
            ans.append(prefix_xor[right+1]^prefix_xor[left])

        return ans