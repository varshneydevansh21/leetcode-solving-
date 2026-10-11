import math


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left, right = 1, max(piles)
        result = max(piles)
        while left <= right:
            mid = (left + right) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / mid)
            if hours <= h:
                result = mid
                right = mid - 1
            else:
                left = mid + 1
        return result