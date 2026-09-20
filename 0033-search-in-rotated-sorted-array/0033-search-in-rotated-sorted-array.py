class Solution:
    def search(self, nums: list[int], target: int) -> int:
        n = len(nums)
        low, high = 0, n - 1
        
        while low <= high:
            mid = (low + high) // 2
            
            if nums[mid] == target:
                return mid
            
            # 1. Left half is sorted
            if nums[low] <= nums[mid]:
                # Check if target is inside the left half bounds
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
                    
            # 2. Right half is sorted
            else:
                # Check if target is inside the right half bounds
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
                    
        return -1