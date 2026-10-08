class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        t_subset = 1 << n
        ans = []
        for num in range(0, t_subset):
            st = []
            for i in range(0, n):
                if num & (1 << i) != 0:
                    st.append(nums[i])
            ans.append(st)
        return ans
