class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            # If the character is a closing bracket
            if char in bracket_map:
                # Pop the top element if stack isn't empty, otherwise assign a dummy value '#'
                top_ele = stack.pop() if stack else '#'
                
                # If the popped element doesn't match the corresponding opening bracket
                if bracket_map[char] != top_ele:
                    return False
            else:
                # If it's an opening bracket, push it onto the stack
                stack.append(char)
                
        # If the stack is empty, all brackets were matched correctly
        return len(stack) == 0