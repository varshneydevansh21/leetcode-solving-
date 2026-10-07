class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        int_max = 2**31 - 1
        int_min = -2**31

        if dividend == int_min and divisor == -1:
            return int_max

        is_negative = (dividend < 0) ^ (divisor < 0)

        dividend = abs(dividend)
        divisor = abs(divisor)
        quotient = 0
        while dividend >= divisor:
            temp_divisor = divisor
            count = 1
            while dividend >= (temp_divisor << 1):
                temp_divisor <<= 1
                count <<= 1
            dividend -= temp_divisor
            quotient += count
        return -quotient if is_negative else quotient