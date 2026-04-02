class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #dp [i] = equals the min amount of coins needed to make up the ith value
        dp = [amount + 1] * (amount + 1)
        dp [0] = 0

        for val in range (1, amount+1): 
            for coin in coins: 
                if val-coin >= 0: 
                    #the coin fits within the val
                    dp [val] = min (dp [val], dp [val-coin] + 1)

        return dp[amount] if dp [amount] != amount + 1 else -1