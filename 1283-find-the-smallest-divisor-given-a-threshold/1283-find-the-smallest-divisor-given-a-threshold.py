import math


class Solution:
    def smallestDivisor(self, nums: list[int], threshold: int) -> int:
        low, high = 1, max(nums)
        ans = high
        while low <= high:
            mid = (low + high) // 2
            total_sum = sum(math.ceil(num / mid) for num in nums)
            if total_sum <= threshold:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans
