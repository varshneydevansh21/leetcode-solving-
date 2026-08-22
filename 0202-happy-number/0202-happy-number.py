class Solution:
    def get_sum_square(self, n: int):
        num = n
        temp = 0
        while num > 0:
            temp += (num % 10) ** 2
            num = num // 10
        return temp

    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = self.get_sum_square(n)
        return n == 1
