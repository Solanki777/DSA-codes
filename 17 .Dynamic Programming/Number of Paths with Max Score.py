
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