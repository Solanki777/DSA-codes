import heapq

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        row=len(grid)
        col=len(grid[0])
        distance=[[float('inf')] * col for _ in range(row)]

        if grid[0][0]==1:
            return -1
        

        
        queue=[([0,0],1)]
        distance[0][0]=1

        while queue:
            curr_node,curr_dist=heapq.heappop(queue)

            i,j=curr_node

            if i ==row-1 and j==col-1:
                return curr_dist
            
            neb=[[-1,0],[0,-1],[1,0],[0,1],[1,1],[-1,-1],[-1,1],[1,-1]]
            for neg in neb:
                new_i,new_j=neg[0]+i,neg[1]+j

                if  0<=new_i<row and 0<=new_j<col and grid[new_i][new_j]==0 :

                    
                    new_dist=curr_dist+1

                    if new_dist<distance[new_i][new_j]:
                        distance[new_i][new_j]=new_dist
                        heapq.heappush(queue,([new_i,new_j],new_dist))
        
        if distance[row-1][col-1]==float('inf'):
            return -1
        
        return distance[row-1][col-1]
    
# since here we apply sorting so time complexity is O(m*n *log m*n) and space complexity is o(m*n)
# optimal solution 

from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0]==1:
            return -1
        
        row,col=len(grid),len(grid[0])
        visited=[[-1]*col for _ in range(row)]
        queue=deque()

        queue.append(((0,0),1))
        neb=[(1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]

        while queue:
            curr_node,curr_dist=queue.popleft()
            i,j=curr_node
            

            if i==row-1 and j==col-1:
                return curr_dist
            
            for n in neb:
                new_i,new_j=i+n[0],j+n[1]
                if 0<=new_i<row and 0<=new_j<col and visited[new_i][new_j]==-1 and grid[new_i][new_j]==0:
                    visited[new_i][new_j]=1
                    queue.append(((new_i,new_j),curr_dist+1))

        return -1

# TIme and space complexity is o(m*n)