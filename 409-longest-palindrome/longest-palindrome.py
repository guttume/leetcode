class Solution:
    def longestPalindrome(self, s: str) -> int:
        size = 26 * 2
        track = [0] * size
        done = False
        ans = 0

        for letter in s:
            pos = ord(letter) - ord('a') if letter in 'abcdefghijklmnopqrstuvwxyz' else 26 + ord(letter) - ord('A')
            track[pos] += 1
            
        for i in range(size):
            if track[i] % 2 == 0:
                continue
            if track[i] % 2 == 1:
                if done == False:
                    done = True
                    continue
                else:
                    track[i] -= 1
                    
        for i in range(size):
            ans += track[i]
            
        return ans