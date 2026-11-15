class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        MOD = 10**9 + 7
        even_count = 1  # empty prefix has even sum
        odd_count = 0
        prefix_odd = False
        ans = 0

        for x in arr:
            prefix_odd ^= x & 1

            if prefix_odd:
                ans += even_count
                odd_count += 1
            else:
                ans += odd_count
                even_count += 1
        return ans % MOD
