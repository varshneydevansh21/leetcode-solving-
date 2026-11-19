class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        s1, s2, s3 = heapq.nsmallest(3, nums)
        l1, l2, l3 = heapq.nlargest(3, nums)
        return min(l1-s3,l2-s2,l3-s1)