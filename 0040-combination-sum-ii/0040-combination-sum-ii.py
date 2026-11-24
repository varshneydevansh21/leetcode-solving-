class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        result = []
        subset = []

        def backtrack(index, total):
            if total == target:
                result.append(subset.copy())
                return

            if total > target:
                return

            for i in range(index, len(candidates)):
                # Skip duplicate choices at the same level
                if i > index and candidates[i] == candidates[i - 1]:
                    continue

                subset.append(candidates[i])
                backtrack(i + 1, total + candidates[i])
                subset.pop()

        backtrack(0, 0)
        return result