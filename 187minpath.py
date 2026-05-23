# recrusion solution TLE time complexity is O(2*(m+n)) and space complexity is O(m+n) for every function called for matrix element stored in recursion stack
class Solution:
    def recursion(self,i,j,m,n,grid):

        if i==0 and j==0:
            return grid[i][j]
        if i<0 or j<0:
            return float('inf')
        
        up=self.recursion(i-1,j,m,n,grid)
        left=self.recursion(i,j-1,m,n,grid)

        return grid[i][j]+min(left,up)

    def minPathSum(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        return self.recursion(m-1,n-1,m,n,grid)

# dp solution :
class Solution:
    def recursion(self,i,j,m,n,grid,dp):

        if i==0 and j==0:
            return grid[i][j]
        if i<0 or j<0:
            return float('inf')
        
        if dp[i][j]!=-1:
            return dp[i][j]
        
        up=self.recursion(i-1,j,m,n,grid,dp)
        left=self.recursion(i,j-1,m,n,grid,dp)

        dp[i][j]= grid[i][j]+min(left,up)

        return dp[i][j]

    def minPathSum(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        dp=[[-1 for _ in range(n)] for _ in range(m)]
        return self.recursion(m-1,n-1,m,n,grid,dp)
    
# tabulation time complexity is O(m*n) and space complexity is O(m*n)
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m=len(grid[0])
        n=len(grid)
        dp=[[-1 for _ in range(m)] for _ in range(n)]
        dp[0][0]=grid[0][0]
        for i in range(n):
            for j in range(m):
                if i==0 and j==0:
                    continue
                
                down=float('inf')
                right=float('inf')
                if i>0:
                    down=dp[i-1][j]
                if j>0:
                    right=dp[i][j-1]

                dp[i][j]=grid[i][j]+min(down,right)
        return dp[n-1][m-1]


# improved space complexity
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m=len(grid[0])
        n=len(grid)
        prev=[0]*m
        curr=[-1]*m
        curr[0]=grid[0][0]
        for i in range(n):
            for j in range(m):
                if i==0 and j==0:
                    continue
                
                down=float('inf')
                right=float('inf')
                if i>0:
                    down=prev[j]
                if j>0:
                    right=curr[j-1]

                curr[j]=grid[i][j]+min(down,right)
            prev=curr
        return prev[m-1]

       