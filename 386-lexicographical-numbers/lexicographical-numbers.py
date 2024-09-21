class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        nums = list(map(str, [i for i in range(1, n + 1)]))

        nums.sort()

        return map(int, nums)