class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        max_prod, min_prod, result = nums[0],nums[0],nums[0]
        
        
        for i in range(1,len(nums)):
            crr = nums[i]
            if crr < 0:
                max_prod, min_prod = min_prod, max_prod
            max_prod = max(crr, max_prod*crr)
            min_prod = min(crr, min_prod*crr)
            result = max(result, max_prod)
        return result