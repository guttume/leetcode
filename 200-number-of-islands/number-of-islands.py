class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()

        ROWS, COLS = len(grid), len(grid[0])

        islands = 0

        def dfs(r, c, rows, cols):
            if (r, c) in visited or min(r, c) < 0 or r >= rows or c >= cols or grid[r][c] == "0":
                return

            if grid[r][c] == "1":
                visited.add((r, c))
                dfs(r + 1, c, rows, cols)
                dfs(r, c + 1, rows, cols)
                dfs(r - 1, c, rows, cols)
                dfs(r, c - 1, rows, cols)

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in visited or grid[r][c] == "0":
                    continue
                
                if grid[r][c] == "1":
                    visited.add((r, c))
                    islands += 1
                    dfs(r + 1, c, ROWS, COLS)
                    dfs(r, c + 1, ROWS, COLS)
                    dfs(r - 1, c, ROWS, COLS)
                    dfs(r, c - 1, ROWS, COLS)

        return islands

                

