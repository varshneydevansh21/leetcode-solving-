class Solution:
    def mySqrt(self, x: int) -> int:
        left, ans = 0,0
        right = x
        while left <= right:
            mid = (left + right) // 2
            if mid * mid == x:
                ans = mid
                return ans
            elif mid * mid < x:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans