class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

    def addWord(self, word):
        cur = self
        for w in word:
            if w not in cur.children:
                cur.children[w] = TrieNode()
            cur = cur.children[w]
        cur.word = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            root.addWord(word)

        ROWS, COLUMNS = len(board), len(board[0])
        res, visited = set(), set()

        def dfs(r, c, node, word):
            if r not in range(ROWS) or c not in range(COLUMNS) or board[r][c] not in node.children or (r, c) in visited:
                return

            visited.add((r,c))

            word += board[r][c]

            if node.children[board[r][c]].word:
                res.add(word)

            if len(res) == len(words):
                return

            dfs(r + 1, c, node.children[board[r][c]], word)
            dfs(r - 1, c, node.children[board[r][c]], word)
            dfs(r, c + 1, node.children[board[r][c]], word)
            dfs(r, c - 1, node.children[board[r][c]], word)

            visited.remove((r, c))

        for i in range(ROWS):
            for j in range(COLUMNS):
                dfs(i, j, root, "")

        return list(res)