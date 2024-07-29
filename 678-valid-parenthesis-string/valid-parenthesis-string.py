class Solution:
    def checkValidString(self, s: str) -> bool:
        # Track the minimum and maximum balance of parentheses
        min_balance = 0
        max_balance = 0

        for c in s:
            if c == '(':
                min_balance += 1
                max_balance += 1
            elif c == ')':
                min_balance -= 1
                max_balance -= 1
            else:  # c == '*'
                min_balance -= 1
                max_balance += 1
            
            # Ensure min_balance does not drop below 0
            if min_balance < 0:
                min_balance = 0
            
            # If max_balance drops below 0, it's invalid
            if max_balance < 0:
                return False
        
        # The string is valid if min_balance is zero
        return min_balance == 0