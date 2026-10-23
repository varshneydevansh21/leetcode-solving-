class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        n = len(cardPoints)
        if n == k:
            return sum(cardPoints)
            
        left_sum = 0
        right_sum = 0
        
        # Step 1: Calculate the sum of the first k elements on the left
        for i in range(0, k):
            left_sum += cardPoints[i]
            
        maxi = left_sum
        right_idx = n - 1
        
        # Step 2: Swap cards one by one from left to right
        for i in range(k - 1, -1, -1):
            left_sum -= cardPoints[i]
            right_sum += cardPoints[right_idx]
            maxi = max(maxi, left_sum + right_sum)
            right_idx -= 1
            
        return maxi