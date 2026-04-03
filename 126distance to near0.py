# time complexity it O(n^3)

from collections import deque
from typing import List

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        col = len(mat[0])

        def bfs(sr, sc):
            queue = deque()
            queue.append((sr, sc, 0))   # include distance

            visited = [[0]*col for _ in range(rows)]
            visited[sr][sc] = 1

            while queue:
                r, c, dist = queue.popleft()

                if mat[r][c] == 0:
                    return dist

                for l, u in [(-1,0),(0,-1),(1,0),(0,1)]:
                    nr, nc = r + l, c + u
                    if 0 <= nr < rows and 0 <= nc < col and not visited[nr][nc]:
                        visited[nr][nc] = 1
                        queue.append((nr, nc, dist + 1))

            return 0

        for u in range(rows):
            for v in range(col):
                if mat[u][v] == 1:
                    mat[u][v] = bfs(u, v)

        return mat
    
# inseted of 1 take 0 and travers thorugh 0 which make it easy 