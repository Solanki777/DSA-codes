
# time complexity is O(3^2n) and space complexity is O(n)
class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        n=len(board)
        MOD=10**9 + 7

        self.max_score=-1
        self.paths=0

        def dfs(i,j,score):
            if i<0 or j<0 or board[i][j]=='X':
                return
            
            if board[i][j].isdigit():
                score+=int(board[i][j])
            
            if board[i][j]=='E':
                if score > self.max_score:
                    self.max_score=score
                    self.paths=1
                elif score==self.max_score:
                    self.paths+=1
                return 
            
            dfs(i-1,j,score)
            dfs(i,j-1,score)
            dfs(i-1,j-1,score)
        
        dfs(n-1,n-1,0)

        if self.max_score==-1:
            return [0,0]
        
        return [self.max_score,self.paths%MOD]
    
# time and space complexity is O(n*n)
class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        n = len(board)
        dp=[[[-1,0] for _ in range(n)] for _ in range(n)]
        MOD= 10 ** 9 +7

        for i in range(n-1,-1,-1):
            for j in range(n-1,-1,-1):

                if board[i][j]=='X':continue
                if board[i][j]=='S':
                    dp[i][j][0]=0
                    dp[i][j][1]=1
                    continue
    
                if board[i][j]=='E':
                    num=0
                else:
                    num=int(board[i][j])
                
                best=-1
                path=0

                for di,dj in ((i+1,j) , (i+1,j+1) , (i,j+1)):
                     
                    if di>=n or dj >=n : continue
                    if dp[di][dj][0]==-1:continue
                    
                    
                    score,count=dp[di][dj]

                    if score>best:
                        best=score
                        path=count

                    elif score==best:
                        path= (path + count) % MOD
                
                if best!=-1:
                    dp[i][j]=[best + num , path]
        
        return dp[0][0] if dp[0][0][0] != -1 else [0,0]

    


        