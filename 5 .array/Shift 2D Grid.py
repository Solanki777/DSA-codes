class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        row = len(grid)
        col = len(grid[0])
        
        def shift():

            last = grid[-1][-1]

            for i in range(row):
                row_last = grid[i][-1]
                for j in range(col -1 , 0 , -1): grid[i][j] = grid[i][j-1]
                grid[i][0] = last
                last = row_last
        
        for _ in range(k):
            shift()
        
        return grid

                    
# Time complexity is O(row*col*k) and space complexity is O(1)