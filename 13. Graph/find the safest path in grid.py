from collections import deque
import heapq

# Time complexity is O(n^2 log n) and space complexity is O(n^2)
class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # Step 1: Multi-source BFS to compute distance to nearest thief
        dist = [[-1]*n]*n
        q = deque()

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    dist[i][j] = 0
                    q.append((i, j))

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while q:
            r, c = q.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < n and 0 <= nc < n and dist[nr][nc] == -1:
                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr, nc))

        # Step 2: Max-heap to find the safest path
        heap = [(-dist[0][0], 0, 0)]
        visited = [[False] * n for _ in range(n)]

        while heap:
            safe, r, c = heapq.heappop(heap)
            safe = -safe

            if visited[r][c]:
                continue

            visited[r][c] = True

            if r == n - 1 and c == n - 1:
                return safe

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                    new_safe = min(safe, dist[nr][nc])
                    heapq.heappush(heap, (-new_safe, nr, nc))

        return 0