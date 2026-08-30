class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # 1. Get the total sum of the array (using Python's built-in sum function)
        total_sum = sum(nums)
        
        # 2. Initialize our running left_sum to 0
        left_sum = 0
        
        # 3. Loop through the array, keeping track of the index (i) and the number (num)
        for i, num in enumerate(nums):
            
            # Check if left_sum equals right_sum (which you correctly identified as total_sum - left_sum - num)
            if left_sum == total_sum - left_sum - num:
                return i  # We found the leftmost pivot!
            
            # If not, add the current number to left_sum for the next iteration
            left_sum += num
            
        # 4. If the loop finishes and we never returned an index, no pivot exists
        return -1