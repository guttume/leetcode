class Solution:
    def shortestPalindrome(self, s: str) -> str:
         # Create a new string that is s + a separator + the reverse of s
        rev_s = s[::-1]
        combined = s + "#" + rev_s
        
        # Build the KMP table for the combined string
        n = len(combined)
        lps = [0] * n
        j = 0  # length of the previous longest prefix suffix
        
        for i in range(1, n):
            while (j > 0 and combined[i] != combined[j]):
                j = lps[j - 1]
            if combined[i] == combined[j]:
                j += 1
            lps[i] = j
        
        # Length of the longest palindromic prefix
        longest_palindrome_prefix_len = lps[-1]
        
        # Characters to add in front of the original string
        non_palindrome_suffix = s[longest_palindrome_prefix_len:]
        
        # Form the shortest palindrome
        shortest_palindrome = non_palindrome_suffix[::-1] + s
        
        return shortest_palindrome