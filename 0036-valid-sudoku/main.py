from collections import defaultdict
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        blocks = defaultdict(set)

        for row in range(9):
            for col in range(9):
                value = board[row]
                if value == ".":
                    continue
                if value in rows[row]:
                    return False
                if value in cols[col]:
                    return False 
                if value in blocks[(row//3, col//3)]:
                    return False
                rows[row].add(value)
                cols[col].add(value)
                blocks[(row//3, col//3)].add(value)
        
        return len(rows) == 9 and len(cols) == 9 and len(blocks) == 9


