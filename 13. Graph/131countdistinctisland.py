#User function Template for python3

import sys
from typing import List
from collections import deque
sys.setrecursionlimit(10**8)
class Solution:
    def countDistinctIslands(self, grid : List[List[int]]) -> int:
        row=len(grid)
        col=len(grid[0])
        shapes=set()

        for i in range(row):
            for j in range(col):
                if grid[i][j]==1:
                    queue=deque()
                    queue.append((i,j))
                    
                    grid[i][j]=0
                    shape=[]
                    
                    base_r,base_c=i,j
                    shape.append((base_r-i,base_c-j))
                    

                    while queue:
                        r,c=queue.popleft()
                        

                        for dx,dy in ([-1,0],[0,-1],[1,0],[0,1]):
                            new_r=r+dx
                            new_c=c+dy
                            if new_r<0 or new_c<0 or new_r>=row or new_c>=col:
                                continue
                            if grid[new_r][new_c]==1:
                                grid[new_r][new_c]=0
                                queue.append((new_r,new_c))
                                shape.append((base_r-new_r,base_c-new_c))
                    shapes.add(tuple(shape))
                    
                        
                    
        return len(shapes)
    

# time complexity is O(n*m) space complexity is O(n*m)