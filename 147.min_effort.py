
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        row=len(heights)
        col=len(heights[0])
        efforts=[[float('inf')*col] for _ in range(row)]
        

        