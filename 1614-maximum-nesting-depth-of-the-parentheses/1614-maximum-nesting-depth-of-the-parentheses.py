class Solution:
    def maxDepth(self, s: str) -> int:
        current_dept = 0
        max_dept = 0
        for char in s:
            if char == '(':
                current_dept +=1
                max_dept = max(max_dept,current_dept)                
            elif char == ')':
                current_dept -=1
        return max_dept