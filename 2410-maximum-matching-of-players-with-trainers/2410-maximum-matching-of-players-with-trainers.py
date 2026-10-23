class Solution:
    def matchPlayersAndTrainers(self, players: list[int], trainers: list[int]) -> int:
        players.sort()
        trainers.sort()
        n = len(players)
        m = len(trainers)
        count = 0
        left, right = 0, 0
        while left < n and right < m:
            if players[left] <= trainers[right]:
                count += 1
                left += 1
            right += 1
        return count