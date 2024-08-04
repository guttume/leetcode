class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []

        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        while left < right and top < bottom:

            # get the elements in the top row
            for i in range(left, right):
                ans.append(matrix[top][i])
            top += 1
            
            # get the elements in the right column
            for i in range(top, bottom):
                ans.append(matrix[i][right - 1])
            right -= 1

            if left >= right or top >= bottom:
                break

            # get the elements in the botton row
            for i in range(right - 1, left - 1, -1):
                ans.append(matrix[bottom - 1][i])
            bottom -= 1

            # get the elements in the left column
            for i in range(bottom - 1, top - 1, -1):
                ans.append(matrix[i][left])
            left += 1

        return ans

            
