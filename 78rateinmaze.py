class Solution:
    def solve(self, maze, row, col, ans, result):
        n = len(maze)
        
        # 1. Out of upper boundary
        if row < 0:
            return
        
        # 2. Out of left boundary
        if col < 0:
            return
        
        # 3. Out of lower boundary
        if row >= n:
            return
        
        # 4. Out of right boundary
        if col >= n:
            return
        
        # 5. Blocked cell
        if maze[row][col] == 0:
            return
        
        # 6. Destination reached
        if row == n-1 and col == n-1:
            result.append("".join(ans))
            return
        
        # Mark current cell as visited (in-place)
        maze[row][col] = 0
        
        # Move Down
        ans.append('D')
        self.solve(maze, row+1, col, ans, result)
        ans.pop()
        
        # Move Left
        ans.append('L')
        self.solve(maze, row, col-1, ans, result)
        ans.pop()
        
        # Move Right
        ans.append('R')
        self.solve(maze, row, col+1, ans, result)
        ans.pop()
        
        # Move Up
        ans.append('U')
        self.solve(maze, row-1, col, ans, result)
        ans.pop()
        
        # Unmark the cell (Backtracking restore)
        maze[row][col] = 1

    def ratInMaze(self, maze):
        result = []
        
        # If starting cell is blocked
        if maze[0][0] == 0:
            return []
        
        self.solve(maze, 0, 0, [], result)
        return sorted(result)
    
# by checking there is 1 or not 
class Solution:
    def solve(self,maze,col,row,ans,result):

        # if there is no option of any where like below is zero above is zero so just return so we put at current postition zero as visited 
        if maze[row][col]==0:
            return 

        # we reached at destination
        if col==len(maze[0])-1 and row==len(maze)-1:
            result.append("".join(ans))
            return
        
        # now it is visited
        maze[row][col]=0
        
        # move down 
        if row+1<len(maze) and maze[row+1][col]==1:
            ans.append('D')
            self.solve(maze,col,row+1,ans,result)
            ans.pop()
        
        # move left
        if col-1>=0 and maze[row][col-1]==1:
            ans.append('L')
            self.solve(maze,col-1,row,ans,result)
            ans.pop()
        
        # move right
        if col+1<len(maze[0]) and maze[row][col+1]==1:
            ans.append('R')
            self.solve(maze,col+1,row,ans,result)
            ans.pop()
        
        # move up 
        if row-1>=0 and maze[row-1][col]==1:
            ans.append('U')
            self.solve(maze,col,row-1,ans,result)
            ans.pop()
        
        # backtracing
        maze[row][col]=1


        


    def ratInMaze(self, maze):
        n = len(maze)
        result = []
        
        # If start is blocked
        if maze[0][0] == 0:
            return []
        
        self.solve(maze, 0, 0, [], result,)
        return sorted(result)

# time complexity is 4*(row*col) and space compelxit (recursion depth)*n*n  stack space