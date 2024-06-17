class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Dictionary to store the results of subproblems
        memo = {}

        def dp(n):
            # Base cases
            if n in memo:
                return memo[n]
            if n == 0:
                return 0
            if n < 0:
                return -1

            # Initialize the minimum number of coins to infinity
            min_coins = float('inf')

            # Try each coin and find the minimum number of coins needed
            for coin in coins:
                res = dp(n - coin)
                if res >= 0 and res < min_coins:
                    min_coins = res + 1

            # Store the result in the memo dictionary
            memo[n] = min_coins if min_coins != float('inf') else -1
            return memo[n]

        return dp(amount)
