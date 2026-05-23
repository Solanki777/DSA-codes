# TLE:TIme complexity is (2*n) for n number of levels and space complexity is n for n depth of the matrix it go
class Solution:
    def recursion(self, i, j, triangle, n):
        
        if i == n - 1:
            return triangle[i][j]

        # it never go outside of the matrix in the move of down and diagonal so no need of if conditions
        down = self.recursion(i + 1, j, triangle, n)

        
        diagonal = self.recursion(i + 1, j + 1, triangle, n)

        return triangle[i][j] + min(down, diagonal)

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        return self.recursion(0, 0, triangle, n)

# using dp + recurison (TLE): TIme complexity is O(n*2)  where n is number in dp and each number has 2 states and space complexity is O(n) recurison stack+ dp (n^2)
class Solution:
    def recursion(self, i, j, triangle, n,dp):

        if dp[i][j]!=-1:
            return dp[i][j]
        
        if i == n - 1:
            return triangle[i][j]
        
        down = self.recursion(i + 1, j, triangle, n,dp)

        
        diagonal = self.recursion(i + 1, j + 1, triangle, n,dp)

        dp[i][j]= triangle[i][j] + min(down, diagonal)
        return dp[i][j]

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)

        # first pick row by row then after picking  read each row length puth that times -1
        dp=[[-1]*len(row) for row in triangle]
        return self.recursion(0, 0, triangle, n,dp)