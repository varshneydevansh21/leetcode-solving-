class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        
        # Helper function: Can we split the array into 'k' or fewer parts 
        # without any part exceeding 'guessed_max_sum'?
        def can_split(guessed_max_sum):
            current_sum = 0
            subarrays_needed = 1  # We always start with at least 1 subarray
            
            for num in nums:
                # If adding the current number exceeds our guess, we MUST make a cut
                if current_sum + num > guessed_max_sum:
                    subarrays_needed += 1
                    current_sum = num  # Start the new subarray with the current number
                    
                    # If making this cut means we have too many subarrays, the guess fails
                    if subarrays_needed > k:
                        return False
                else:
                    current_sum += num
                    
            return True

        # Set the boundaries for Binary Search
        left = max(nums)   # The absolute smallest the answer could ever be
        right = sum(nums)  # The absolute largest the answer could ever be
        best_answer = right
        
        # Binary Search loop
        while left <= right:
            mid = (left + right) // 2  # This is our current "guessed_max_sum"
            
            if can_split(mid):
                # The guess worked! We can successfully split the array.
                # Save this answer, but see if we can find an even smaller one.
                best_answer = mid
                right = mid - 1
            else:
                # The guess failed (forced us to make too many cuts). 
                # Our guess was too small, so we must search higher.
                left = mid + 1
                
        return best_answer