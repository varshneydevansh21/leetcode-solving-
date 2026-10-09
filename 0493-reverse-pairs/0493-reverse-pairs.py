class Solution:
    def reversePairs(self, nums):
        def count_pairs(low, mid, high):
            cnt = 0
            j = mid + 1
            for i in range(low, mid + 1):
                while j <= high and nums[i] > 2 * nums[j]:
                    j += 1
                cnt += j - (mid + 1)
            return cnt

        def merge(low, mid, high):
            temp = []
            left, right = low, mid + 1
            while left <= mid and right <= high:
                if nums[left] <= nums[right]:
                    temp.append(nums[left]); left += 1
                else:
                    temp.append(nums[right]); right += 1
            temp.extend(nums[left:mid + 1])
            temp.extend(nums[right:high + 1])
            nums[low:high + 1] = temp

        def merge_sort(low, high):
            if high <= low:
                return 0
            mid = (low + high) // 2
            cnt = merge_sort(low, mid) + merge_sort(mid + 1, high)
            cnt += count_pairs(low, mid, high)
            merge(low, mid, high)
            return cnt

        return merge_sort(0, len(nums) - 1)