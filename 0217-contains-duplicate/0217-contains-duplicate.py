class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        element_log = set()
        for i in nums:
            if i in element_log:
                return True 
            else:
                element_log.add(i)
        return False