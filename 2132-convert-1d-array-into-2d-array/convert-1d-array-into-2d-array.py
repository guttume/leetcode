class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m * n != len(original):
            return []

        ans = []
        
        temp = []
        for i in range(len(original)):
            if i % n == 0 and i > 0:
                ans.append(temp)
                temp = []
            temp.append(original[i])
        
        ans.append(temp)
        return ans