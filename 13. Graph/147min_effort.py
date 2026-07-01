
import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        row=len(heights)
        col=len(heights[0])
        efforts=[[float('inf')]*col for _ in range(row)]

        efforts[0][0]=0
        heap=[(0,(0,0))]
        neb=[(0,1),(1,0),(-1,0),(0,-1)]

        while heap:
            ef,curr_node=heapq.heappop(heap)
            i=curr_node[0]
            j=curr_node[1]
            if ef > efforts[i][j]:
                continue
            if i == row-1 and j == col-1:
                return ef

            for n in neb:
                new_i,new_j=i+n[0],j+n[1]
                

                if 0<=new_i<row and 0<=new_j<col and efforts[new_i][new_j]>max(ef,abs(heights[i][j]-heights[new_i][new_j])):
                    new_effort=max(ef,abs(heights[i][j]-heights[new_i][new_j]))

                    heapq.heappush(heap,(new_effort,(new_i,new_j)))
                    efforts[new_i][new_j]=new_effort
        
        return efforts[row-1][col-1]

            



# Time Complexity	O(m × n log(m × n)) and Space Complexity O(m × n)

        

        