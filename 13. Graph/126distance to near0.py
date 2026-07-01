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
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        row=len(mat)
        col=len(mat[0])

        ans=[[0 for _ in range(col)] for _ in range(row)]
        visited=[[0 for _ in range(col)] for _ in range(row)]

        queue=deque()

        for i in range(row):
            for j in range(col):
                if mat[i][j]==0:
                    queue.append((i,j,0))
                    visited[i][j]=1
        
        while queue:
            r,c,d=queue.popleft()
            ans[r][c]=d

            for dx,dy in [[-1,0],[0,-1],[1,0],[0,1]]:
                new_r=dx+r
                new_c=dy+c
                if 0<=new_r<row and 0<=new_c<col and visited[new_r][new_c]==0:
                    visited[new_r][new_c]=1
                    queue.append((new_r,new_c,d+1))
        return ans

# time complexity and space complexity is O(m*n) 

        