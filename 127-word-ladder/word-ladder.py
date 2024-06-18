class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        nbors = collections.defaultdict(list)

        wordList.append(beginWord)

        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                nbors[pattern].append(word)

        q = deque([beginWord])
        visited = set([beginWord])

        res = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res

                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]

                    for n in nbors[pattern]:
                        if n not in visited:
                            visited.add(n)
                            q.append(n)

            res += 1

        return 0
