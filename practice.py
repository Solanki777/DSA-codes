class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        row=len(boxGrid)
        col=len(boxGrid[0])
        ans= [[0]*row for _ in range(col)]

        for i in range(row):
            for j in range(col):
                ans[j][row-1-i]=boxGrid[i][j]
        
        
        for i in range(col):
            m,n=-1,-1
            for j in range(row-1,-1,-1):
                if ans[i][j]==".":
                    m,n=i,j

                if ans[i][j]=="*":
                    m,n=-1,-1

                if ans[i][j]=="#":
                    if m!=-1:
                        ans[m][n]="#"
                        ans[i][j]="."
                        n-=1
                        
        return ans
        