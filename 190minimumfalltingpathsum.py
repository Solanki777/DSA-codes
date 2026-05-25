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