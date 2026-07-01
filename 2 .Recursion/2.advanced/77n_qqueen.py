# from typing import List
# class Solution:
#     def isvalid(self,board,col,n,row):

#         # row check 
#         tempcol=col
#         while tempcol>=0:
#             if board[row][tempcol]=="Q":
#                 return False
#             tempcol-=1

#         tempcol=col
#         temprow=row

#         # uper diagonal check 
#         while tempcol>=0 and temprow>=0:
#             if board[temprow][tempcol]=="Q":
#                 return False
#             tempcol-=1
#             temprow-=1
        
#         temprow=row
#         tempcol=col
#         # lower diagnoal
#         while tempcol>=0 and temprow<=n-1:
#             if board[temprow][tempcol]=="Q":
#                 return False
#             tempcol-=1
#             temprow+=1

#         return True
        

#     def solve(self,board,col,n,ans):
#         if col==n:
#             temp=["".join(board[i]) for i in range(n)]
#             ans.append(temp)
#             return

#         for row in range(n):
#             if self.isvalid(board,col,n,row):
#                 board[row][col]="Q"
#                 self.solve(board,col+1,n,ans)
#                 board[row][col]="."
            

        
#     def solveNQueens(self, n: int) -> List[List[str]]:        
#         board=[["."]*n for _ in range(n)]
#         # print(board)
#         ans=[]
#         self.solve(board,0,n,ans)
#         return ans

# n=5
# print(Solution().solveNQueens(n))

# time complexity is O(n!*n) where n! is for each qeen find but other n is for etrating n elemnts in board to check there is any queen or not 

# otimal solution 
from typing import List
class Solution:
    def isvalid(self,board,col,n,row,rowcheck,updiagonal,lowdiagonal):
        if rowcheck[row]==1:
            return False
        if updiagonal[row+col]==1:
            return False
        if lowdiagonal[col-row+(n-1)]==1:
            return False
        return True

        

    def solve(self,board,col,n,ans,rowcheck,updiagonal,lowdiagonal):
        if col==n:
            temp=["".join(board[i]) for i in range(n)]
            ans.append(temp)
            return

        for row in range(n):
            if self.isvalid(board,col,n,row,rowcheck,updiagonal,lowdiagonal):

                # place queen 
                board[row][col]="Q"
                rowcheck[row]=1
                updiagonal[row+col]=1
                lowdiagonal[(n-1)+col-row]=1
                self.solve(board,col+1,n,ans,rowcheck,updiagonal,lowdiagonal)

                # undo queen 
                board[row][col]="."
                rowcheck[row]=0
                updiagonal[row+col]=0
                lowdiagonal[(n-1)+col-row]=0
            

        
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        rowccheck=[0]*n
        upediagonlcheck=[0]*(2*n-1)
        lowdiagonlcheck=[0]*(2*n-1)

        board=[["."]*n for _ in range(n)]
        # print(board)
        ans=[]
        self.solve(board,0,n,ans,rowccheck,upediagonlcheck,lowdiagonlcheck)
        return ans

n=5
print(Solution().solveNQueens(n))
