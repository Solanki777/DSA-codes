
# pure recursion O(2^(m+n)) and space comlexity is O(m+n)
class Solution:
    def recursion(self,matrix,m,n,i,j):
        if i>=m or j>=n:
            return 0
        
        if matrix[i][j]==1:
            return 0
        
        if i==m-1 and j==n-1:
            return 1
        
        
        return self.recursion(matrix,m,n,i+1,j)+self.recursion(matrix,m,n,i,j+1)
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        return self.recursion(obstacleGrid,m,n,0,0)

# using dp time complexity is O(m*n) and space complexity is dp o(m*n) + o(m+n) recursion stack

class Solution:
    def recursion(self,matrix,m,n,i,j,dp):
        if i>=m or j>=n:
            return 0
        
        if matrix[i][j]==1:
            return 0
        
        if i==m-1 and j==n-1:
            return 1
        
        if dp[i][j]!=0:
            return dp[i][j]
        
        
        dp[i][j]=self.recursion(matrix,m,n,i+1,j,dp)+self.recursion(matrix,m,n,i,j+1,dp)

        return dp[i][j]
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        dp=[[0 for _ in range(n)] for _ in range(m)]
        return self.recursion(obstacleGrid,m,n,0,0,dp)