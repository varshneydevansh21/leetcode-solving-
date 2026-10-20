class Solution:

  def threeSumClosest(self, nums: list[int], target: int) -> int:
    # Step 1: Sort the array to enable the two-pointer technique
    nums.sort()
    n = len(nums)

    # Initialize closest_sum with the sum of the first three elements
    closest_sum = nums[0] + nums[1] + nums[2]

    # Step 2: Iterate through the array
    for i in range(n - 2):
      # Optimization: Skip duplicate outer elements to avoid redundant work
      if i > 0 and nums[i] == nums[i - 1]:
        continue

      left, right = i + 1, n - 1

      # Step 3: Use two pointers for the remaining elements
      while left < right:
        current_sum = nums[i] + nums[left] + nums[right]

        # If we find an exact match, it can't get any closer than 0 difference
        if current_sum == target:
          return target

        # Update closest_sum if the current sum is closer to the target
        if abs(current_sum - target) < abs(closest_sum - target):
          closest_sum = current_sum

        # Move pointers based on comparison with target
        if current_sum < target:
          left += 1
        else:
          right -= 1

    return closest_sum