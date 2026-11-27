class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        MAX_FACTOR = 1500

        freq = [0] * (MAX_FACTOR + 1)
        for factor, _ in items:
            freq[factor] += 1

        # cnt[f] = number of item types whose factor is divisible by f
        cnt = [0] * (MAX_FACTOR + 1)
        for f in range(1, MAX_FACTOR + 1):
            for multiple in range(f, MAX_FACTOR + 1, f):
                cnt[f] += freq[multiple]

        dp = [0] * (budget + 1)

        for factor, price in items:
            bonus = cnt[factor] - 1

            # Buy the first copy: activates the item and gives its bonus.
            # Traverse budget downward so this item is activated at most once.
            for b in range(budget, price - 1, -1):
                dp[b] = max(dp[b], dp[b - price] + 1 + bonus)

            # Buy additional copies: each adds exactly one copy.
            # Traverse budget upward for the unbounded-knapsack transition.
            for b in range(price, budget + 1):
                dp[b] = max(dp[b], dp[b - price] + 1)

        return dp[budget]