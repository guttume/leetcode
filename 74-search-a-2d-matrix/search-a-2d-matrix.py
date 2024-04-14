class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lr, rr = 0, len(matrix) - 1
        row = (lr + rr) // 2

        while lr <= rr:
            mr = (lr + rr) // 2

            if target > matrix[mr][-1]:
                lr = mr + 1
            elif target < matrix[mr][0]:
                rr = mr - 1
            else:
                row = mr
                break

        l, r = 0, len(matrix[row]) - 1

        while l <= r:
            mid = (l + r) // 2

            if target > matrix[row][mid]:
                l = mid + 1
            elif target < matrix[row][mid]:
                r = mid - 1
            else:
                return True
        
        return False