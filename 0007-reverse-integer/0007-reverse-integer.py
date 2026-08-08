class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1 
        reverse_x = int(str(abs(x))[::-1])*sign
        if -2**31 <= reverse_x <= 2**31 - 1:
            return reverse_x
        else:
            return 0