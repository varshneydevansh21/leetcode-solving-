class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        maxi = 0
        L = 0
        zeros = 0

        for R in range(len(nums)):
            if nums[R] == 0:
                zeros += 1

            while zeros > k:
                if nums[L] == 0:
                    zeros -= 1
                L += 1

            maxi = max(maxi, R - L + 1)

        return maxi