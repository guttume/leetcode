class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word_length = 0
        
        for i in range(len(s)):
            if i != 0 and s[i - 1] == " " and s[i] != " ":
                word_length = 1
            elif s[i] != " ":
                word_length += 1


        return word_length