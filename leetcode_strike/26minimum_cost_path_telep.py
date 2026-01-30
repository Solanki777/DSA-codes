
# this is solution but it take large time it give TLE now we try to reduce the size of dp to get soltuion in optimal way
# class Solution:
#     def find_ans(self, dp, i, j, grid, l, k):
#         row, col = len(grid), len(grid[0])

#         # reached destination → no more cost
#         if i == row - 1 and j == col - 1:
#             return 0

#         if dp[i][j][l] != -1:
#             return dp[i][j][l]

#         result = float('inf')
#         curval=grid[i][j]

#         # move right
#         if j + 1 < col:
#             result = min(
#                 result,
#                 grid[i][j+1] + self.find_ans(dp, i, j+1, grid, l, k)
#             )

#         # move down
#         if i + 1 < row:
#             result = min(
#                 result,
#                 grid[i+1][j] + self.find_ans(dp, i+1, j, grid, l, k)
#             )

#         # teleport (zero cost + condition)
#         if l < k:
#             for x in range(row):
#                 for y in range(col):
#                     if (x!=i or y!=j) and grid[x][y]<=curval:

#                         result = min(
#                             result,
#                             self.find_ans(dp, x, y, grid, l+1, k)
#                         )

#         dp[i][j][l] = result
        
#         return result

#     def minCost(self, grid, k):
#         row, col = len(grid), len(grid[0])
#         dp = [[[-1] * (k+1) for _ in range(col)] for _ in range(row)]
        
#         return self.find_ans(dp,0,0,grid,0,k)
class Solution:
    def minCost(self, grid, k):
        row= len(grid)  #rows
        col= len(grid[0]) #cols

        dp=[[float('inf')]*col for _ in range(row)]
        dp[row-1][col-1]=0

        # cost for destination to destination is zero

        # find maxvalue from grid to make telport aaray
        maxVal=0
        for i in range(row):
            for j in range(col):
                maxVal=max(maxVal,grid[i][j])

        # build the teleport aaray
        tel=[float('inf')]*(maxVal+1)

        # Now traverse the matrix 
        for t in range(k+1):
            for i in range(row-1,-1,-1):
                for j in range(col-1,-1,-1):
                    if i+1 < row :
                        dp[i][j]=min(dp[i][j],grid[i+1][j] + dp[i+1][j])
                            
                        
                    if j+1 < col:
                        dp[i][j]=min( dp[i][j], grid[i][j+1] + dp[i][j+1])
                    
                    if t>0:
                        dp[i][j]=min(dp[i][j],tel[grid[i][j]])
                            
                        
            # update the telportcost array
            for i in range(row):
                for j in range(col):
                    tel[grid[i][j]]=min(tel[grid[i][j]],dp[i][j])
            
            for i in range(1,len(tel)):
                tel[i]=min(tel[i],tel[i-1])
        return dp[0][0]





s=Solution()
print(s.minCost([[1,3,3],[2,5,4],[4,3,5]],2))
