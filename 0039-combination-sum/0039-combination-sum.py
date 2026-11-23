class Solution:
    def solve(self, index, total, subset, nums, target, result):
        # Base case: If the running total matches the target, record the current subset
        if total == target:
            result.append(subset.copy())  # Add a copy to avoid future modifications
            return
        # Pruning: If the running total exceeds the target, stop this path
        elif total > target:
            return
        # Base case: If we have considered all candidates, terminate this branch
        if index >= len(nums):
            return

        # Choice 1: Include the candidate at the current index (allowing reuse)
        Sum = total + nums[index]
        subset.append(nums[index])
        self.solve(index, Sum, subset, nums, target, result)  # Same index for reuse

        # Backtrack: Remove the candidate just added
        Sum = total  # Reset Sum to the value before including the candidate
        subset.pop()

        # Choice 2: Skip the candidate and move to the next index
        self.solve(index + 1, Sum, subset, nums, target, result)

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        self.solve(0, 0, [], candidates, target, result)
        return result