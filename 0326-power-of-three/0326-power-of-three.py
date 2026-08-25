class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        for x in range(31):
            if n == 3**x:
                return True
        return False
