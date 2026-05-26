# recursion solution: time complexity is O(3^r) and space complexity O(r)
class Solution:
    def recursion(self,i,j,r,c,matrix):
        if j<0 or j>=c:
            return float('inf')

        if i==r-1:
            return matrix[i][j]

        down_left=self.recursion(i+1,j-1,r,c,matrix)
        down=self.recursion(i+1,j,r,c,matrix)
        down_right=self.recursion(i+1,j+1,r,c,matrix)

        return matrix[i][j]+min(down_left,down,down_right)

    def minFallingPathSum(self, matrix: List[List[int]]) -> int:

        r,c=len(matrix),len(matrix[0])
        ans=float('inf')

        for j in range(c):
            ans=min(ans,self.recursion(0,j,r,c,matrix))

        return ans

# dp + recurison : time complexity is O(r*c) and space complexity is (r*c + r recursive stake)
class Solution:
    def recursion(self,i,j,r,c,matrix,dp):
        if j<0 or j>=c:
            return float('inf')
        
        if dp[i][j]!=-1:
            return dp[i][j]

        if i==r-1:
            return matrix[i][j]

        down_left=self.recursion(i+1,j-1,r,c,matrix,dp)
        down=self.recursion(i+1,j,r,c,matrix,dp)
        down_right=self.recursion(i+1,j+1,r,c,matrix,dp)

        dp[i][j]= matrix[i][j]+min(down_left,down,down_right)
        return dp[i][j]

    def minFallingPathSum(self, matrix: List[List[int]]) -> int:

        r,c=len(matrix),len(matrix[0])
        dp=[[-1 for _ in range(c)] for _ in range(r)]
        ans=float('inf')

        for j in range(c):
            ans=min(ans,self.recursion(0,j,r,c,matrix,dp))

        return ans

# tabulation solution time and space complexity is O(r*c)
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:

        r,c=len(matrix),len(matrix[0])
        dp=[[-1 for _ in range(c)] for _ in range(r)]

        for i in range(c):
            dp[0][i]=matrix[0][i]

        for i in range(1,r):
            for j in range(c):
                
                movedown=matrix[i-1][j]

                moveright=float('inf')
                if j-1>0:
                    moveright=matrix[i-1][j-1]
                
                moveleft=float('inf')
                if j+1<c:
                    moveleft=matrix[i-1][j+1]
                dp[i][j]=min(movedown,moveleft,moveright)
        
        return min(dp[r-1])
    
# optimized space complexity to O(c)
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:

        r,c=len(matrix),len(matrix[0])
        prev=[-1 for _ in range(c)] 

        for i in range(c):
            prev[i]=matrix[0][i]

        for i in range(1,r):
            curr=[-1]*c
            for j in range(c):
                
                movedown=prev[j]

                moveright=float('inf')
                if j-1>=0:
                    moveright=prev[j-1]
                
                moveleft=float('inf')
                if j+1<c:
                    moveleft=prev[j+1]
                curr[j]=matrix[i][j]+min(movedown,moveleft,moveright)
            prev=curr
        
        return min(prev)