class Solution:
    def jump(self, nums: List[int]) -> int:
        q = deque()
        v = set()

        q.append(0)
        v.add(0)

        count = 0

        while q:
            for i in range(len(q)):
                index = q.popleft()

                if index == len(nums) - 1:
                    return count

                for j in range(1, nums[index] + 1):
                    if index + j not in v:
                        q.append(index+j)
                        v.add(index+j)

            count += 1
