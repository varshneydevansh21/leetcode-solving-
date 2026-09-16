class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        n = len(nums)
        ans = []
        nums.sort()
        
        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # EARLY STOP 1: The smallest possible sum is too large
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break
            
            # EARLY STOP 2: The largest possible sum is too small
            if nums[i] + nums[n - 3] + nums[n - 2] + nums[n - 1] < target:
                continue
                
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                
                # EARLY STOP 3: Min sum for this 'j' is too large
                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                    break
                    
                # EARLY STOP 4: Max sum for this 'j' is too small
                if nums[i] + nums[j] + nums[n - 2] + nums[n - 1] < target:
                    continue
                
                k = j + 1
                l = n - 1
                
                while k < l:
                    total = nums[i] + nums[j] + nums[k] + nums[l]
                    
                    if total == target:
                        ans.append([nums[i], nums[j], nums[k], nums[l]])
                        k += 1
                        l -= 1
                        
                        while k < l and nums[k] == nums[k - 1]:
                            k += 1
                        while l > k and nums[l] == nums[l + 1]:
                            l -= 1
                            
                    elif total < target:
                        k += 1
                    else:
                        l -= 1
                        
        return ans