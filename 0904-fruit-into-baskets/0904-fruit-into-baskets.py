class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        count = {}
        L = 0
        maxi = 0

        for R in range(len(fruits)):
            count[fruits[R]] = count.get(fruits[R], 0) + 1

            while len(count) > 2:
                count[fruits[L]] -= 1
                if count[fruits[L]] == 0:
                    del count[fruits[L]]
                L += 1

            maxi = max(maxi, R - L + 1)

        return maxi