class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
            
        mappings = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        ans = []

        def backtrack(index: int, path: str):
            if index == len(digits):
                ans.append(path)
                return

            for char in mappings[digits[index]]:
                backtrack(index + 1, path + char)

        backtrack(0, "")

        return ans
    
        
            