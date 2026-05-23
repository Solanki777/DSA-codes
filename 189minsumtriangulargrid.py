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