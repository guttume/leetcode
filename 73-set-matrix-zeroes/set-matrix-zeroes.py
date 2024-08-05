class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])
        col0 = 1

        # First pass: use first row and column to mark zeroes
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    if c > 0:
                        matrix[0][c] = 0
                    else:
                        col0 = 0

        # Second pass: use markers to set cells to zero
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

        # Check if the first row needs to be zeroed
        if matrix[0][0] == 0:
            for c in range(cols):
                matrix[0][c] = 0

        # Check if the first column needs to be zeroed
        if col0 == 0:
            for r in range(rows):
                matrix[r][0] = 0
