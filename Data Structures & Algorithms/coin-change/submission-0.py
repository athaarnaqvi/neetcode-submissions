class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = [[-1] * (amount + 1) for _ in range(len(coins))]

        def solve(i, total):
            if total == 0:
                return 0

            if total < 0:
                return float('inf')

            if i >= len(coins):
                return float('inf')

            if cache[i][total] != -1:
                return cache[i][total]

            take = 1 + solve(i, total - coins[i])
            skip = solve(i + 1, total)

            cache[i][total] = min(take , skip)
            return cache[i][total]

        
        ans = solve(0, amount)
        if ans == float('inf'):
            return -1
        return ans