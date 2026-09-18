class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        count1, count2 = 0, 0
        candidate1, candidate2 = None, None
        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1 = num
                count1 = 1
            elif count2 == 0:
                candidate2 =  num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
        real_count1, real_count2 = 0, 0
        threshold = len(nums) // 3
        for num in nums:
            if num == candidate1:
                real_count1 += 1
            elif num == candidate2:
                real_count2 += 1

        result = []
        if real_count1 > threshold:
            result.append(candidate1)
        if real_count2 > threshold:
            result.append(candidate2)
        return result
