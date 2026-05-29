# pure recursion: time coplexity is O(3^n * 3 ^n) and space complexity is O(r)
class Solution:
    def recursion(self,grid,row,col,r,c1,c2):
        if c1<0 or c1>=col or c2<0 or c2>=col:
            return float('-inf')
        
        
        if r==row-1:
            if c1==c2:
                return grid[r][c1]
            return grid[r][c1]+grid[r][c2]
        
        maxi=float('-inf')
        for i in range(-1,2):
            for j in range(-1,2):
                newc1=c1+i
                newc2=c2+j

                if c1==c2:
                    ans=self.recursion(grid,row,col,r+1,newc1,newc2)+grid[r][c1]
                else:
                    ans=self.recursion(grid,row,col,r+1,newc1,newc2)+grid[r][c1]+grid[r][c2]
                maxi=max(maxi,ans)
        return maxi
        

    def cherryPickup(self,grid):
        m=len(grid)
        n=len(grid[0])
        return self.recursion(grid,m,n,0,0,n-1)

# dp solution  Time complexi is O(rows*cols*cols*9) and space complexity is O(rows*col*col) dp + recursion stack O(row)
class Solution:
    def recursion(self,grid,row,col,r,c1,c2,dp):
        
        if c1<0 or c1>=col or c2<0 or c2>=col:
            return float('-inf')

        if dp[r][c1][c2]!=-1:
            return dp[r][c1][c2]
        
        if r==row-1:
            if c1==c2:
                return grid[r][c1]
            return grid[r][c1]+grid[r][c2]
        
        maxi=0
        for i in range(-1,2):
            for j in range(-1,2):
                new_c1=c1+i
                new_c2=c2+j

                if c1==c2:
                    ans=self.recursion(grid,row,col,r+1,new_c1,new_c2,dp)+grid[r][c1]
                else:
                    ans=self.recursion(grid,row,col,r+1,new_c1,new_c2,dp)+grid[r][c1]+grid[r][c2]
                maxi=max(maxi,ans)
        dp[r][c1][c2]=maxi
        return dp[r][c1][c2]
                

    def cherryPickup(self, grid: List[List[int]]) -> int:
        row=len(grid)
        col=len(grid[0])
        dp=[[[-1 for _ in range(col)] for _ in range(col)] for _ in range(row)]
 
        return self.recursion(grid,row,col,0,0,col-1,dp)

# tabulation time complexity is O(row*col*col*9) and spac complexity is O(row*col*col)
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        row=len(grid)
        col=len(grid[0])
        dp=[[[-1 for _ in range(col)] for _ in range(col)] for _ in range(row)]

        for i in range(col):
            for j in range(col):
                if i==j:
                    dp[row-1][i][j]=grid[row-1][j]
                else:
                    dp[row-1][i][j]=grid[row-1][j]+grid[row-1][i]

        for r in range(row-2,-1,-1):
            for c1 in range(col):
                for c2 in range(col):
                    maxi=0
                    for i in range(-1,2):
                        for j in range(-1,2):
                            new_c1=c1+i
                            new_c2=c2+j

                            if 0<=new_c1<col and 0<=new_c2<col:
                                if c1==c2:
                                    ans=grid[r][c1]
                                else:
                                    ans=grid[r][c1]+grid[r][c2]
                                ans+=dp[r+1][new_c1][new_c2]
                                maxi=max(maxi,ans)
                    dp[r][c1][c2]=maxi
        return dp[0][0][col-1]
        
# improved space complexity time complexity is O(row*col*col*9) and spac complexity is O(col*col)
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        row=len(grid)
        col=len(grid[0])

       
        last=[[-1 for _ in range(col)] for _ in range(col)]
        

        for i in range(col):
            for j in range(col):
                if i==j:
                    last[i][j]=grid[row-1][j]
                else:
                    last[i][j]=grid[row-1][j]+grid[row-1][i]

        for r in range(row-2,-1,-1):
            curr=[[-1 for _ in range(col)] for _ in range(col)]
            for c1 in range(col):
                for c2 in range(col):
                    maxi=0
                    for i in range(-1,2):
                        for j in range(-1,2):
                            new_c1=c1+i
                            new_c2=c2+j

                            if 0<=new_c1<col and 0<=new_c2<col:
                                if c1==c2:
                                    ans=grid[r][c1]
                                else:
                                    ans=grid[r][c1]+grid[r][c2]
                                ans+=last[new_c1][new_c2]
                                maxi=max(maxi,ans)
                    curr[c1][c2]=maxi
            last=curr
        return last[0][col-1]
        
        