#User function Template for python3

from typing import List
from collections import deque
class Solution:    
    def minimumMultiplications(self, arr : List[int], start : int, end : int) -> int:
        MOD=100000
        distance=[float('inf')]*MOD
        ans=float('inf')
        queue=deque()
        queue.append((start,0))
        distance[0]=0

        while queue:
            node,step=queue.popleft()

            if node==end:
                return step

            for neb in arr:
                new_mult=(node*neb)%MOD
                new_step=step+1
                if distance[new_mult]>new_step:
                    queue.append((new_mult,new_step))
                    distance[new_mult]=new_step
        return -1

# Time complexity is O(10000 * len(arr)) and space complexity is Space Complexity=O(100000)

        