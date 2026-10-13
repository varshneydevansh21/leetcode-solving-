class Solution:
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        if len(bloomDay) < m * k:
            return -1
        low = min(bloomDay)
        high = max(bloomDay)

        def can_make(days: int) -> bool:
            streak = 0
            total_bqt = 0
            for bloom in bloomDay:
                if bloom <= days:
                    streak += 1
                    if streak == k:
                        streak = 0
                        total_bqt += 1
                else:
                    streak = 0
            return total_bqt >= m

        while low <= high:
            mid = (low + high) // 2
            if can_make(mid):
                ans = mid 
                high = mid - 1
            else: 
                low = mid + 1

        return ans