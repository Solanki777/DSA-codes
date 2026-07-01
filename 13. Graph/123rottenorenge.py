from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        row=len(grid)
        col=len(grid[0])
        queue=deque([])
        fresh_count=0
        minute=0

        for i in range(row):
            for j in range(col):
                if grid[i][j]==2:
                    queue.append([i,j])
                if grid[i][j]==1:
                    fresh_count+=1
        
        while queue and fresh_count>0:
            for _ in range(len(queue)):

                i,j=queue.popleft()



                for dx , dy in ([[-1,0],[0,-1],[1,0],[0,1]]):
                    new_i=i+dx
                    new_j=j+dy

                    if new_i<0 or new_j<0 or new_i==row or new_j==col:
                        continue
                    if grid[new_i][new_j]==0 or grid[new_i][new_j]==2:
                        continue

                    grid[new_i][new_j]=2
                    queue.append([new_i,new_j])
                    fresh_count-=1
            minute+=1
        
        if fresh_count>0:
            return -1
        return minute
    
# time complexity and space complexity is  O(m*n)


    





