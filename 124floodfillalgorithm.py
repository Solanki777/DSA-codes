
# using bfs 
from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc]==color:
            return image
        
        row=len(image)
        col=len(image[0])
        ori=image[sr][sc]

        queue=deque()
        queue.append((sr,sc))
        image[sr][sc]=color

        while queue:
            i,j=queue.popleft()
            for dx,dy in ([-1,0],[0,-1],[1,0],[0,1]):
                new_i=i+dx
                new_j=j+dy
                if 0<=new_i<row and 0<=new_j<col:
                    if image[new_i][new_j]==ori:
                        image[new_i][new_j]=color
                        queue.append((new_i,new_j))
        return image

# time and space complexity is O(m*n)

# using dfs
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        row=len(image)
        col=len(image[0])
        change=image[sr][sc]

        if color==image[sr][sc]:
            return image
        def dfs(i,j):
            if i<0 or j<0 or i==row or j==col:
                return
            
            if image[i][j]!=change:
                return
            
            image[i][j]=color
            dfs(i+1,j)
            dfs(i,j+1)
            dfs(i-1,j)
            dfs(i,j-1)
            
        dfs(sr,sc)
        return image
            



