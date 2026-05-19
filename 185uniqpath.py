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
        
        