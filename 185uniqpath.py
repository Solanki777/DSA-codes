# pure recursion  time complexity is 2^(m+n) and space complexiitiy is O(m+n)
class Solution:
    def recursion(self,m,n,i,j):
        if i==m-1 and j==n-1:
            return 1
        
        if i>=m or j>=n:
            return 0
        
        return self.recursion(m,n,i+1,j)+self.recursion(m,n,i,j+1)    
    
    def uniquePaths(self, m: int, n: int) -> int:
        return self.recursion(m,n,0,0)
    
# dp + recursion TIme and space complexity is O(m*n)+O(m+n)
class Solution:
    def recursion(self,m,n,i,j,dp):
        
        if i>m-1 or j>n-1:
            return 0
        if i==m-1 or j==n-1:
            return 1
        if dp[i][j]!=0:
            return dp[i][j]
        dp[i][j]=self.recursion(m,n,i+1,j,dp)+self.recursion(m,n,i,j+1,dp)
        return dp[i][j]
        
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[0 for _ in range(n)] for _ in range(m)]
        return self.recursion(m,n,0,0,dp)

# tabulation time and space complexity is O(m*n)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[0 for _ in range(n)] for _ in range(m)]
        dp[m-1][n-1]=1
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if i==m-1 and j==n-1:
                    continue
                down=0
                left=0
                if i+1<m:
                    down=dp[i+1][j]
                if j+1<n:
                    left=dp[i][j+1]

                dp[i][j]=down+left
                
        return dp[0][0]
    

# space optimization time complexity is O(m) and space complexity is O(1)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prev=[0]*n
        for i in range(m-1,-1,-1):
            curr=[0]*n
            for j in range(n-1,-1,-1):
                if i==m-1 and j==n-1:
                    curr[j]=1
                else:
                    down=prev[j]
                    right=0
                    if j+1<n:
                        right=curr[j+1]
                    curr[j]=down+right
            prev=curr
        return curr[0]
              
        
        
