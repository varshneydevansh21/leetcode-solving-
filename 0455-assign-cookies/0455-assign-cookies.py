class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g.sort()
        s.sort()
        n = len(g)
        m = len(s)
        count = 0
        left, right = 0, 0
        while left < n and right < m:
            if g[left] <= s[right]:
                count += 1
                left += 1
            right += 1
        return count