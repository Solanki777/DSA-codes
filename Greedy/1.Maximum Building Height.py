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

# instead of traversing all values now we traveerse only restrected values and calulate the same way as above

# time complexity is O(m log m) and space complexity is O(1)
class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        restrictions.append([1,0])
        if not any(idx == n for idx, _ in restrictions):
            restrictions.append([n, n - 1])
        restrictions.sort()

        for  i in range(1,len(restrictions)):

            diff=restrictions[i][0]-restrictions[i-1][0]
            restrictions[i][1]=min(restrictions[i][1],restrictions[i-1][1]+diff)
        
        for i in range(len(restrictions)-2,-1,-1):
            diff=restrictions[i+1][0]-restrictions[i][0]
            restrictions[i][1]=min(restrictions[i][1],restrictions[i+1][1]+diff)

        ans=0
        for i in range(1,len(restrictions)):
            x1,h1=restrictions[i-1]
            x2,h2=restrictions[i]
            
            dist=x2-x1
            ans=max(ans,(h1+h2+dist)//2)
        return ans
            

        