class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        q = collections.deque()

        seconds = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]== 2:
                    q.append((r, c, 0))

        while q:
            for i in range(len(q)):
                r, c, time = q.popleft()

                seconds = time

                directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

                for dr, dc in directions:
                    next_row, next_col = r + dr, c + dc

                    if 0 <= next_row < ROWS and 0 <= next_col < COLS and grid[next_row][next_col] == 1:
                        grid[next_row][next_col] = 2
                        q.append((next_row, next_col, time + 1))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return -1

        return seconds

        