# TLE for long size of building constraints

class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        store={}
        store[1]=0
        for i in range(2,n+1):
            store[i]=i-1
        
        for indx,height in restrictions:
            store[indx]=min(store[indx],height)

        for i in range(2,n+1):
            store[i]=min(store[i],store[i-1]+1)
        
        for i in range(n-1,0,-1):
            store[i]=min(store[i],store[i+1]+1)
        
        ans=0
        for i in range(1,n+1):
            ans=max(ans,store[i])

        return ans

        