class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        tpe =[]
        for i in range(0,31):
            tpe.append(2**i)
        left = 0 
        right = len(tpe) - 1
        while left <= right:
            mid = (left + right)//2 
            if tpe[mid] == n:
                return True
            elif tpe[mid] < n: 
                left = mid + 1
            else: 
                right = mid - 1
        return False 