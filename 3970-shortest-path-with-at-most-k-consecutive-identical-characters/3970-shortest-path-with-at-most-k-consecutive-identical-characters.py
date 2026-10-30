import heapq
from collections import defaultdict
from math import inf

class Solution:
    def shortestPath(
        self,
        n: int,
        edges: list[list[int]],
        labels: str,
        k: int,
    ) -> int:
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))

        # dist[node][run], where run is 1-indexed
        dist = [[inf] * (k + 1) for _ in range(n)]
        dist[0][1] = 0

        heap = [(0, 0, 1)]  # cost, node, current consecutive run

        while heap:
            cost, u, run = heapq.heappop(heap)

            if cost > dist[u][run]:
                continue

            if u == n - 1:
                return cost

            for v, w in graph[u]:
                new_run = run + 1 if labels[u] == labels[v] else 1

                if new_run > k:
                    continue

                new_cost = cost + w
                if new_cost < dist[v][new_run]:
                    dist[v][new_run] = new_cost
                    heapq.heappush(heap, (new_cost, v, new_run))

        return -1