
# using dfs 
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        col=len(grid[0])
        row=len(grid)
        visited=[[0 for i in range(col)] for j in range(row)]
        
        ans=0

        def dfs(i,j):
            if i<0 or i>=row or j<0 or j>=col:
                return
            if visited[i][j]==1 or grid[i][j]=="0":
                return
            if visited[i][j]==0 and grid[i][j]=="1":
                visited[i][j]=1
            dfs(i+1,j)
            dfs(i,j+1)
            dfs(i-1,j)
            dfs(i,j-1)
            return


        for i in range(row):
            for j in range(col):
                if visited[i][j]==0 and grid[i][j]=="1":
                    ans+=1
                    dfs(i,j)
        return ans
    


# using bfs
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row=len(grid)
        col=len(grid[0])
        ans=0

        for i in range(row):
            for j in range(col):
                if grid[i][j]=="1":
                    queue=deque()
                    queue.append((i,j))
                    grid[i][j]="0"
                    ans+=1

                    while queue:
                        r,c=queue.popleft()

                        for dx,dy in ([-1,0],[0,-1],[1,0],[0,1]):
                            new_r=r+dx
                            new_c=c+dy
                            if new_r<0 or new_c<0 or new_r>=row or new_c>=col:
                                continue
                            if grid[new_r][new_c]=="1":
                                grid[new_r][new_c]="0"
                                queue.append((new_r,new_c))
        return ans
# time and space complexity is O(m*n)
# but dfs has promblem of recursion call stack overfloaw 
        
        