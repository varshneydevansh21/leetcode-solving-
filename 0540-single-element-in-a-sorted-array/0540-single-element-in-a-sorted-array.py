class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        
        while low < high:
            mid = (low + high) // 2
            
            # This single line checks mid+1 if mid is even, and mid-1 if mid is odd!
            if nums[mid] == nums[mid ^ 1]:
                low = mid + 1
            else:
                high = mid
                
        return nums[low]