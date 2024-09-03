class Solution:
    def getLucky(self, s: str, k: int) -> int:
        digit_sum = 0
        for c in s:
            val = int(str(ord(c) - ord('a') + 1))
            while val > 0:
                val, rem = divmod(val, 10)
                digit_sum += rem
    
        while k > 1 and digit_sum >= 10:
            temp = 0
            while digit_sum > 0:
                digit_sum, rem = divmod(digit_sum, 10)
                temp += rem
            k -= 1
            digit_sum = temp

        return digit_sum

        
