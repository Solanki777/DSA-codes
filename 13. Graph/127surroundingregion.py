class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows=len(board)
        cols=len(board[0])

        def dfs(r,c):
            
            if r>=rows or r<0 or c>=cols or c<0:
                return 
            if visited[r][c]==1:
                return
            if board[r][c]=='X':
                return
            
            visited[r][c]=1
                
            
            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c-1)
            dfs(r,c+1)
            







        visited=[[0 for _ in range(cols)]for _ in range(rows)]


        for i in range(cols):
            if visited[0][i]==0 and board[0][i]=='O':
                dfs(0,i)
        
        for j in range(rows):
            if visited[j][0]==0 and board[j][0]=='O':
                dfs(j,0)
        
        for k in range(cols):
            if visited[rows-1][k]==0 and board[rows-1][k]=='O':
                dfs(rows-1,k)
        
        for l in range(rows):
            if visited[l][cols-1]==0 and board[l][cols-1]=='O':
                dfs(l,cols-1)

        for i in range(rows):
            for j in range(cols):
                if visited[i][j]==0 and board[i][j]=='O':
                    board[i][j]='X'

# Time ocmplexity is O(2(r+c)+r*c)==(rc) and space complexity is same 
        