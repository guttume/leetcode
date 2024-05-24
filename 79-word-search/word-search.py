class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(x, y, k):
            if x < 0 or y < 0 or x >= len(board) or y >= len(board[0]) or board[x][y] != word[k]:
                return False
            if k == len(word) - 1:
                return True
            temp = board[x][y]
            board[x][y] = "#"  # Mark the cell as visited
            found = dfs(x + 1, y, k + 1) or dfs(x - 1, y, k + 1) or dfs(x, y + 1, k + 1) or dfs(x, y - 1, k + 1)
            board[x][y] = temp  # Revert the cell back
            return found

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True

        return False