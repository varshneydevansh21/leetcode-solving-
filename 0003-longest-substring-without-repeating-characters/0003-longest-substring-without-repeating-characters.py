class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans_dict = {}
        left, right, maxi = 0, 0, 0
        n = len(s)
        while right < n:
            if s[right] in ans_dict:
                left = max(left, ans_dict[s[right]] + 1)
            maxi = max(maxi, right - left + 1)
            ans_dict[s[right]] = right
            right += 1
        return maxi
