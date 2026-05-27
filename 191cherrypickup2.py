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

        for i in [-1,0,1]:
            for j in [-1,0,1]:

                new_c1=c1+i
                new_c2=c2+j

                if c1==c2:
                    curr=grid[r][c1]
                else:
                    curr=grid[r][c1]+grid[r][c2]

                ans=curr+self.recursion(grid,row,col,r+1,new_c1,new_c2)

                maxi=max(maxi,ans)

        return maxi

    def cherryPickup(self,grid):
        row=len(grid)
        col=len(grid[0])

        return self.recursion(grid,row,col,0,0,col-1)