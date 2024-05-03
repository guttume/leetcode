class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        index = -1
        ans = ""
        for i, c in enumerate(word):
            if ch == c:
                index = i
                break

        if index == -1:
            return word

        ans = word[index::-1] + word[index+1:]

        return ans