from collections import deque

# Time complexity and space complexity is O(n^2) 
class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        d=deque()
        r=len(grid)
        c=len(grid[0])

        heal=[[-1 for _ in range(c)] for _ in range(r)]

        start=health-grid[0][0]
        if start<=0:
            return False

        d.append((0,0,start))
        heal[0][0]=start
        directions=[(0,1),(1,0),(-1,0),(0,-1)]

        while d:
            i,j,h=d.popleft()
            if i==r-1 and j==c-1 and h>0:
                return True
             
            
            
            for dr , dc in directions:
                nr=i+dr
                nc=j+dc

                if 0<=nr<r and 0<=nc<c :
                    new_h=h-grid[nr][nc]
                                       
                    if new_h >0 and new_h > heal[nr][nc]:
                        heal[nr][nc]=new_h
                        d.append((nr,nc,new_h))


        return False
        




        