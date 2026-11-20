from typing import List

class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        nums.sort()
        dp = {}  # dp[v] = longest consecutive run ending at value v
        ans = 0

        for x in nums:
            # Use x as x + 1
            dp[x + 1] = max(dp.get(x + 1, 0), dp.get(x, 0) + 1)

            # Keep x unchanged
            dp[x] = max(dp.get(x, 0), dp.get(x - 1, 0) + 1)

            ans = max(ans, dp[x + 1], dp[x])

        return ans