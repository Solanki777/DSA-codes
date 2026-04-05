class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        
        row=len(grid)
        col=len(grid[0])


        def dfs(r,c):
            if r<0 or r>=row or c<0 or c>=col:
                return
            if visited[r][c]==1 or grid[r][c]==0:
                return
            
            visited[r][c]=1
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c-1)
            dfs(r,c+1)

        visited=[[0 for _ in range (col)] for _ in range(row)]

        for i in range(col):
            if visited[0][i]==0 and grid[0][i]:
                dfs(0,i)

        for i in range(col):
            if visited[row-1][i]==0 and grid[row-1][i]:
                dfs(row-1,i)

        for i in range(row):
            if visited[i][0]==0 and grid[i][0]:
                dfs(i,0)

        for i in range(row):
            if visited[i][col-1]==0 and grid[i][col-1]:
                dfs(i,col-1)
        
        ans=0
        for i in range(row):
            for j in range(col):
                if grid[i][j] and visited[i][j]==0:
                    ans+=1
        return ans
      

# Time and space ocmplexity is O(m*n)